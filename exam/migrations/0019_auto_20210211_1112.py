# Generated by Django 3.0.2 on 2021-02-11 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0018_auto_20210211_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exams',
            name='coursenamefkey',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='examanswer',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='examanswer1',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='examanswer1_true',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='examanswer2',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='examanswer2_true',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='examanswer3',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='examanswer3_true',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='examanswer4',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='examanswer4_true',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='examanswer_published',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='examfileanswer_published',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='examfileaudio',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='examfileaudio_published',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='examfilepic',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='examfilepic_published',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='examfiletext',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='examfiletext_published',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='examfilevideo',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='examfilevideo_published',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='examlinkaudio',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='examlinkaudio_published',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='examlinkpic',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='examlinkpic_published',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='examlinkvideo',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='examlinkvideo_published',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='examquestion',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='examquestion_published',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='examtext',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='examtext_published',
        ),
    ]
