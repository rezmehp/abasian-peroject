# Generated by Django 3.0.2 on 2020-07-13 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0013_auto_20200713_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exams2',
            name='trueanswer',
            field=models.TextField(max_length=1, verbose_name='شماره گزینه صحیح از 1 تا 4'),
        ),
    ]
