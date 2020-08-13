# Generated by Django 3.0.2 on 2020-08-13 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20200713_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='advertise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic_hru', models.ImageField(upload_to='advertise/photos/%y/%m/%d/', verbose_name='عکس هدر سمت راست بالا')),
                ('hru', models.CharField(max_length=2000, verbose_name='لینک هدر سمت راست بالا')),
                ('pic_hlu', models.ImageField(upload_to='advertise/photos/%y/%m/%d/', verbose_name='عکس هدر سمت چپ بالا')),
                ('hlu', models.CharField(max_length=2000, verbose_name='لینک هدر سمت چپ بالا')),
                ('pic_hrd', models.ImageField(upload_to='advertise/photos/%y/%m/%d/', verbose_name='عکس هدر سمت راست پایین')),
                ('hrd', models.CharField(max_length=2000, verbose_name='لینک هدر سمت راست پایین')),
                ('pic_hld', models.ImageField(upload_to='advertise/photos/%y/%m/%d/', verbose_name='عکس هدر سمت چپ پایین')),
                ('hld', models.CharField(max_length=2000, verbose_name='لینک هدر سمت چپ پایین')),
                ('pic_fru', models.ImageField(upload_to='advertise/photos/%y/%m/%d/', verbose_name='عکس فوتر سمت راست بالا')),
                ('fru', models.CharField(max_length=2000, verbose_name='لینک فوتر سمت راست بالا')),
                ('pic_flu', models.ImageField(upload_to='advertise/photos/%y/%m/%d/', verbose_name='عکس فوتر سمت چپ بالا')),
                ('flu', models.CharField(max_length=2000, verbose_name='لینک فوتر سمت چپ بالا')),
                ('pic_frd', models.ImageField(upload_to='advertise/photos/%y/%m/%d/', verbose_name='عکس فوتر سمت راست پایین')),
                ('frd', models.CharField(max_length=2000, verbose_name='لینک فوتر سمت راست پایین')),
                ('pic_fld', models.ImageField(upload_to='advertise/photos/%y/%m/%d/', verbose_name='عکس فوتر سمت چپ پایین')),
                ('fld', models.CharField(max_length=2000, verbose_name='لینک فوتر سمت چپ پایین')),
            ],
            options={
                'verbose_name_plural': 'تبلیغات',
            },
        ),
    ]
