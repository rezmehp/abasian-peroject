# Generated by Django 3.0.2 on 2020-03-20 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactadmin',
            name='pic',
            field=models.ImageField(upload_to='contact/photos/%y/%m/%d/'),
        ),
    ]
