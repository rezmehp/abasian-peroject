# Generated by Django 3.0.2 on 2020-09-10 19:28

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0017_auto_20200713_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactuserpayam4',
            name='javabadmin',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='جواب ادمین'),
        ),
        migrations.AlterField(
            model_name='contactuserpm',
            name='javabadmin',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='جواب ادمین'),
        ),
    ]