# Generated by Django 3.0.2 on 2020-09-10 19:44

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classlinks', '0005_allclasslinks3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allclasslinks',
            name='link_about',
            field=ckeditor.fields.RichTextField(verbose_name='توضیحات لینک کلاس'),
        ),
        migrations.AlterField(
            model_name='allclasslinks1',
            name='link_about',
            field=ckeditor.fields.RichTextField(verbose_name='توضیحات کلاس'),
        ),
        migrations.AlterField(
            model_name='allclasslinks2',
            name='link_about',
            field=ckeditor.fields.RichTextField(verbose_name='توضیحات کلاس'),
        ),
        migrations.AlterField(
            model_name='allclasslinks3',
            name='link_about',
            field=ckeditor.fields.RichTextField(verbose_name='توضیحات کلاس'),
        ),
    ]
