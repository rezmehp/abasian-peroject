# Generated by Django 3.0.2 on 2020-09-10 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classlinks', '0006_auto_20200911_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allclasslinks',
            name='link_about',
            field=models.CharField(max_length=3000, verbose_name='توضیحات لینک کلاس'),
        ),
        migrations.AlterField(
            model_name='allclasslinks1',
            name='link_about',
            field=models.CharField(max_length=3000, verbose_name='توضیحات کلاس'),
        ),
        migrations.AlterField(
            model_name='allclasslinks2',
            name='link_about',
            field=models.CharField(max_length=3000, verbose_name='توضیحات کلاس'),
        ),
    ]
