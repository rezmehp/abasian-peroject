# Generated by Django 3.0.2 on 2020-06-18 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_auto_20200617_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='exams',
            name='examfileanswer',
            field=models.FileField(blank=True, upload_to='courseexam/exams/%y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='exams',
            name='examfileanswer_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='exams',
            name='examfiletext',
            field=models.FileField(blank=True, upload_to='courseexam/exams/%y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='exams',
            name='examfiletext_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='exams',
            name='examtext_published',
            field=models.BooleanField(default=True),
        ),
    ]
