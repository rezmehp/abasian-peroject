# Generated by Django 3.0.2 on 2020-09-10 16:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='about',
            field=ckeditor.fields.RichTextField(verbose_name='توضیحات خبر'),
        ),
    ]
