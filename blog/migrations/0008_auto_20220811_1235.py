# Generated by Django 3.2.7 on 2022-08-11 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_sitesetting'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sitesetting',
            options={'verbose_name': 'تنظیم', 'verbose_name_plural': 'تنظیمات'},
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='site_name',
            field=models.CharField(max_length=100, verbose_name='نام سایت'),
        ),
    ]