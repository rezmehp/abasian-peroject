# Generated by Django 3.0.2 on 2020-08-29 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorialvideo', '0007_auto_20200713_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursevideo2',
            name='hazine',
            field=models.IntegerField(verbose_name='هزینه به تومان'),
        ),
    ]
