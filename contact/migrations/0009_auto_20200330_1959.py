# Generated by Django 3.0.2 on 2020-03-30 15:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0008_auto_20200330_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactuserpayam4',
            name='tarikhjavab',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 30, 19, 59, 15, 888331)),
        ),
    ]
