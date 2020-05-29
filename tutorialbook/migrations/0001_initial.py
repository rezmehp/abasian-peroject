# Generated by Django 3.0.2 on 2020-05-29 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0004_modaresin'),
    ]

    operations = [
        migrations.CreateModel(
            name='tutorialbookAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_page', models.CharField(max_length=500)),
                ('pic', models.ImageField(upload_to='tutorialbook/photos/%y/%m/%d/')),
                ('title_search', models.CharField(max_length=500)),
                ('text_click', models.CharField(max_length=500)),
                ('title_1', models.CharField(max_length=500)),
                ('title_2', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='coursebook2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='coursebook/photos/%y/%m/%d/')),
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
            name='books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=1000)),
                ('booklink_is_published', models.BooleanField(default=True)),
                ('booklink', models.CharField(blank=True, max_length=1000)),
                ('bookbook_is_published', models.BooleanField(default=True)),
                ('bookbook', models.FileField(blank=True, upload_to='coursebook/books/%y/%m/%d/')),
                ('coursenamefkey', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tutorialbook.coursebook2')),
            ],
        ),
    ]
