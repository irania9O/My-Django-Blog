# Generated by Django 3.2.7 on 2022-08-13 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_rename_iamge_sitesetting_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_special',
            field=models.BooleanField(default=False, verbose_name='مقاله ویژه'),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('d', 'پیش\u200cنویس'), ('p', 'منتشر شده'), ('i', 'در حال بررسی'), ('b', 'برگشت داده شده')], max_length=1, verbose_name='وضعیت'),
        ),
    ]
