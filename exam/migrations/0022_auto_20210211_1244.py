# Generated by Django 3.0.2 on 2021-02-11 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0021_auto_20210211_1243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examsanswer',
            old_name='coursequestionfkey',
            new_name='coursequestionfokey',
        ),
    ]
