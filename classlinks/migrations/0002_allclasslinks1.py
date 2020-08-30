# Generated by Django 3.0.2 on 2020-08-11 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classlinks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='allclassLinks1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_title', models.CharField(max_length=3000, verbose_name='تیتر کلاس')),
                ('link_about', models.CharField(max_length=3000, verbose_name='توضیحات کلاس')),
                ('link_url', models.CharField(max_length=3000, verbose_name='لینک کلاس')),
                ('link_pic', models.ImageField(upload_to='classlinks/photos/%y/%m/%d/', verbose_name='عکس کلاس')),
                ('link_time', models.TimeField(verbose_name='ساعت برگزاری کلاس')),
                ('link_date', models.TimeField(verbose_name='تاریخ برگزاری کلاس')),
                ('link_price', models.IntegerField(verbose_name='هزینه کلاس')),
            ],
            options={
                'verbose_name_plural': 'لینک کلاس ها',
            },
        ),
    ]