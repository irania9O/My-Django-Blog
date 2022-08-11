from django.db import models
from django.utils import timezone
from extentions.utils import jalali_converter

class SingletonBaseModel(models.Model):
    class Meta:
        verbose_name = "تنظیم"
        verbose_name_plural = "تنظیمات"   
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
class SiteSetting(SingletonBaseModel):
    site_header = models.CharField(max_length=50, verbose_name="هدر سایت", default="هدر سایت")
    site_name = models.CharField(max_length=100, verbose_name="نام سایت", default="نام سایت")
    site_description =  models.CharField(max_length=200, verbose_name="توضیحات سایت", default="توضیحات سایت")

    def __str__(self):
        return 'برای تغیر اطلاعات کلیک کنید.'

class Catagory(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس دسته بندی")
    status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن")
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"   
        ordering = ['position']

    def __str__(self) -> str:
        return self.title
class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش‌نویس'),
        ('p', 'منتشر شده'),
    )
    title = models.CharField(max_length=200, verbose_name="عنوان مقاله")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس مقاله")
    catagory = models.ManyToManyField(Catagory, verbose_name="دسته بندی")
    description = models.TextField(verbose_name="محتوا")
    thumbnail = models.ImageField(upload_to="images", verbose_name="تصویر مقاله")
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ['-publish']

    def __str__(self) -> str:
        return self.title
    
    def jpublish(self):
        return jalali_converter(self.publish)

    jpublish.short_description = "زمان انتشار"

