# Generated by Django 3.0.2 on 2020-05-24 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorialvideo', '0005_auto_20200524_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='videolink',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
