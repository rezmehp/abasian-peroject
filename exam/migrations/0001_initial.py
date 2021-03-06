# Generated by Django 3.0.2 on 2020-06-17 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0005_sliderimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='courseexam2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='courseexam/photos/%y/%m/%d/')),
                ('coursename', models.CharField(max_length=1000)),
                ('saattadris', models.CharField(max_length=1000)),
                ('tozihat', models.TextField()),
                ('hazine', models.IntegerField()),
                ('maghtafkey', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pages.maghtaTahsili')),
                ('modaresinfkey', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pages.modaresin')),
                ('reshteTahsilifkey', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pages.reshteTahsili')),
            ],
        ),
        migrations.CreateModel(
            name='tutorialexamAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_page', models.CharField(max_length=500)),
                ('pic', models.ImageField(upload_to='tutorialexam/photos/%y/%m/%d/')),
                ('title_search', models.CharField(max_length=500)),
                ('text_click', models.CharField(max_length=500)),
                ('title_1', models.CharField(max_length=500)),
                ('title_2', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='exams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examquestion_published', models.BooleanField(default=True)),
                ('examquestion', models.CharField(max_length=50000)),
                ('examanswer1', models.CharField(max_length=50000)),
                ('examanswer2', models.CharField(max_length=50000)),
                ('examanswer3', models.CharField(max_length=50000)),
                ('examanswer4', models.CharField(max_length=50000)),
                ('examtext', models.CharField(blank=True, max_length=50000)),
                ('examlinkpic_published', models.BooleanField(default=True)),
                ('examlinkpic', models.CharField(blank=True, max_length=2000)),
                ('examfilepic_published', models.BooleanField(default=True)),
                ('examfilepic', models.FileField(blank=True, upload_to='courseexam/exams/%y/%m/%d/')),
                ('examlinkvideo_published', models.BooleanField(default=True)),
                ('examlinkvideo', models.CharField(blank=True, max_length=2000)),
                ('examfilevideo_published', models.BooleanField(default=True)),
                ('examfilevideo', models.FileField(blank=True, upload_to='courseexam/exams/%y/%m/%d/')),
                ('examlinkaudio_published', models.BooleanField(default=True)),
                ('examlinkaudio', models.CharField(blank=True, max_length=2000)),
                ('examfileaudio_published', models.BooleanField(default=True)),
                ('examfileaudio', models.FileField(blank=True, upload_to='courseexam/exams/%y/%m/%d/')),
                ('examanswer_published', models.BooleanField(default=True)),
                ('examanswer', models.CharField(blank=True, max_length=50000)),
                ('coursenamefkey', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exam.courseexam2')),
            ],
        ),
    ]
