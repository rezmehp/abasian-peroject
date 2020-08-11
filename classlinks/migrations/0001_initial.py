# Generated by Django 3.0.2 on 2020-08-11 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='allclassLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_title', models.CharField(max_length=3000, verbose_name='تیتر لینک کلاس')),
                ('link_about', models.CharField(max_length=3000, verbose_name='توضیحات لینک کلاس')),
                ('link_url', models.CharField(max_length=3000, verbose_name='لینک کلاس')),
                ('link_pic', models.ImageField(upload_to='classlinks/photos/%y/%m/%d/', verbose_name='عکس لینک کلاس')),
            ],
            options={
                'verbose_name_plural': 'لینک کلاس ها',
            },
        ),
        migrations.CreateModel(
            name='classlinksAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_page', models.CharField(max_length=500, verbose_name='تیتر صفحه')),
                ('pic', models.ImageField(upload_to='classlinks/photos/%y/%m/%d/', verbose_name='عکس بالای صفحه')),
                ('title_classlinks', models.CharField(max_length=500, verbose_name='تیتر لینک کلاس ها')),
            ],
            options={
                'verbose_name_plural': 'تنظیمات صفحه لینک کلاس های آنلاین',
            },
        ),
    ]
