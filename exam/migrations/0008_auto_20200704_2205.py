# Generated by Django 3.0.2 on 2020-07-04 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0007_auto_20200622_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exams',
            name='examanswer1',
            field=models.TextField(max_length=50001),
        ),
    ]
