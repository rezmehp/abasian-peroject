# Generated by Django 3.0.2 on 2020-09-10 19:28

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorialvideo', '0008_auto_20200829_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursevideo2',
            name='tozihat',
            field=ckeditor.fields.RichTextField(verbose_name='توضیحات'),
        ),
    ]
