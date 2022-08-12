# Generated by Django 3.2.7 on 2022-08-11 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20220811_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='site_description',
            field=models.CharField(default='توضیحات سایت', max_length=200, verbose_name='توضیحات سایت'),
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='site_header',
            field=models.CharField(default='هدر سایت', max_length=50, verbose_name='هدر سایت'),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='site_name',
            field=models.CharField(default='نام سایت', max_length=100, verbose_name='نام سایت'),
        ),
    ]