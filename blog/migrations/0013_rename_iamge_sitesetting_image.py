# Generated by Django 3.2.7 on 2022-08-13 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_article_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitesetting',
            old_name='iamge',
            new_name='image',
        ),
    ]