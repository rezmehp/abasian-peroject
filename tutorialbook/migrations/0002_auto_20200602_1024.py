# Generated by Django 3.0.2 on 2020-06-02 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorialbook', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='bookbook',
            new_name='bookfile',
        ),
    ]
