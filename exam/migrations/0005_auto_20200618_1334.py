# Generated by Django 3.0.2 on 2020-06-18 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_auto_20200618_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exams',
            name='examanswer1_true',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='exams',
            name='examanswer2_true',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='exams',
            name='examanswer3_true',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='exams',
            name='examanswer4_true',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='exams',
            name='examanswer_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='exams',
            name='examfileanswer_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='exams',
            name='examfileaudio_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='exams',
            name='examfilepic_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='exams',
            name='examfiletext_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='exams',
            name='examfilevideo_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='exams',
            name='examlinkaudio_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='exams',
            name='examlinkpic_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='exams',
            name='examlinkvideo_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='exams',
            name='examtext_published',
            field=models.BooleanField(default=False),
        ),
    ]
