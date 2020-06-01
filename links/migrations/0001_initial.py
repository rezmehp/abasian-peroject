# Generated by Django 3.0.2 on 2020-05-29 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='allLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_title', models.CharField(max_length=3000)),
                ('link_url', models.CharField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='linksAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_page', models.CharField(max_length=500)),
                ('pic', models.ImageField(upload_to='links/photos/%y/%m/%d/')),
                ('title_links', models.CharField(max_length=500)),
            ],
        ),
    ]