# Generated by Django 3.0.2 on 2020-08-30 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zarinpal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buys',
            name='courseid',
            field=models.CharField(max_length=5000, verbose_name='آیدی درس'),
        ),
        migrations.AlterField(
            model_name='buys',
            name='userid',
            field=models.CharField(max_length=5000, verbose_name='آیدی کاربر'),
        ),
    ]
