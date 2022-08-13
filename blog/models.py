from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.html import format_html 
from account.models import User
from extentions.utils import jalali_converter

# my manager 
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')

class CatagoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)

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
    image = models.ImageField(upload_to="images", verbose_name="تصویر تیتر سایت")

    def __str__(self):
        return 'برای تغیر اطلاعات کلیک کنید.'

class Catagory(models.Model):
    parent = models.ForeignKey('self', default=None , null=True, blank=True, on_delete=models.SET_NULL, related_name='children', verbose_name="زیر دسته")
    title = models.CharField(max_length=200, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس دسته بندی")
    status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن")
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"   
        ordering = ['parent__id', 'position']

    def __str__(self) -> str:
        return self.title
    
    objects = CatagoryManager()
class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش‌نویس'),           # draft
        ('p', 'منتشر شده'),         # publish
        ('i', 'در حال بررسی'),      # investigaion
        ('b', 'برگشت داده شده'),    # back
    )
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="articles", verbose_name="نویسنده")
    title = models.CharField(max_length=200, verbose_name="عنوان مقاله")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس مقاله")
    catagory = models.ManyToManyField(Catagory, verbose_name="دسته بندی", related_name="articles")
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

    def get_absolute_url(self):
        return reverse("account:home")

    def jpublish(self):
        return jalali_converter(self.publish)

    jpublish.short_description = "زمان انتشار"

    objects = ArticleManager()

    def thumbnail_tag(self):
        return format_html(f"<img width=100 height=60 style='border-radius: 5px;' src='{self.thumbnail.url}'>")

    thumbnail_tag.short_description = "عکس"

    def catagoy_to_list(self):
        catagoties = []
        for catagory in self.catagory.active():
            catagoties.append(catagory.title)
        
        if len(catagoties) == 0:
            return "بدون دسته بندی"
        else:
            return "، ".join(catagoties)

    catagoy_to_list.short_description = "دسته بندی"