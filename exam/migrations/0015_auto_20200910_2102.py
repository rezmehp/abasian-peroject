# Generated by Django 3.0.2 on 2020-09-10 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0014_auto_20200713_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseexam2',
            name='hazine',
            field=models.IntegerField(verbose_name='هزینه به تومان'),
        ),
    ]
