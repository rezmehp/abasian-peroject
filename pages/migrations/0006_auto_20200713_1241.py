# Generated by Django 3.0.2 on 2020-07-13 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_sliderimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='footeradmin',
            options={'verbose_name_plural': 'تنظیمات فوتر صفحات'},
        ),
        migrations.AlterModelOptions(
            name='maghtatahsili',
            options={'verbose_name_plural': 'ثبت مقطع'},
        ),
        migrations.AlterModelOptions(
            name='modaresin',
            options={'verbose_name_plural': 'ثبت مدرسین'},
        ),
        migrations.AlterModelOptions(
            name='ostanha',
            options={'verbose_name_plural': 'ثبت استان'},
        ),
        migrations.AlterModelOptions(
            name='reshtetahsili',
            options={'verbose_name_plural': 'ثبت رشته'},
        ),
        migrations.AlterModelOptions(
            name='shahrha',
            options={'verbose_name_plural': 'ثبت شهر'},
        ),
        migrations.AlterModelOptions(
            name='sliderimage',
            options={'verbose_name_plural': 'به روز رسانی عکس های اسلایدر صفحه اول سایت'},
        ),
        migrations.AlterField(
            model_name='footeradmin',
            name='instagram',
            field=models.CharField(max_length=2000, verbose_name='لینک اینستاگرام'),
        ),
        migrations.AlterField(
            model_name='footeradmin',
            name='instagram_published',
            field=models.BooleanField(default=True, verbose_name='نمایش یا عدم نمایش اینستاگرام'),
        ),
        migrations.AlterField(
            model_name='footeradmin',
            name='linkedin',
            field=models.CharField(max_length=2000, verbose_name='لینک لینک این'),
        ),
        migrations.AlterField(
            model_name='footeradmin',
            name='linkedin_published',
            field=models.BooleanField(default=True, verbose_name='نمایش یا عدم نمایش لینک این'),
        ),
        migrations.AlterField(
            model_name='footeradmin',
            name='mail',
            field=models.CharField(max_length=2000, verbose_name='لینک ایمیل'),
        ),
        migrations.AlterField(
            model_name='footeradmin',
            name='mail_published',
            field=models.BooleanField(default=True, verbose_name='نمایش یا عدم نمایش ایمیل'),
        ),
        migrations.AlterField(
            model_name='footeradmin',
            name='telegram',
            field=models.CharField(max_length=2000, verbose_name='لینک تلگرام'),
        ),
        migrations.AlterField(
            model_name='footeradmin',
            name='telegram_published',
            field=models.BooleanField(default=True, verbose_name='نمایش یا عدم نمایش تلگرام'),
        ),
        migrations.AlterField(
            model_name='footeradmin',
            name='title',
            field=models.CharField(max_length=2000, verbose_name='تیتر فوتر صفحات'),
        ),
        migrations.AlterField(
            model_name='footeradmin',
            name='twitter',
            field=models.CharField(max_length=2000, verbose_name='لینک توئیتر'),
        ),
        migrations.AlterField(
            model_name='footeradmin',
            name='twitter_published',
            field=models.BooleanField(default=True, verbose_name='نمایش یا عدم نمایش توئیتر'),
        ),
        migrations.AlterField(
            model_name='footeradmin',
            name='whatsapp',
            field=models.CharField(max_length=2000, verbose_name='لینک واتس اپ'),
        ),
        migrations.AlterField(
            model_name='footeradmin',
            name='whatsapp_published',
            field=models.BooleanField(default=True, verbose_name='نمایش یا عدم نمایش واتس اپ'),
        ),
        migrations.AlterField(
            model_name='maghtatahsili',
            name='maghta',
            field=models.CharField(max_length=100, verbose_name='نام مقطع تحصیلی'),
        ),
        migrations.AlterField(
            model_name='modaresin',
            name='email_modares',
            field=models.CharField(max_length=2000, verbose_name='ایمیل مدرس'),
        ),
        migrations.AlterField(
            model_name='modaresin',
            name='modares',
            field=models.CharField(max_length=300, verbose_name='نام و نام خانوادگی مدرس'),
        ),
        migrations.AlterField(
            model_name='ostanha',
            name='ostanName',
            field=models.CharField(max_length=100, verbose_name='نام استان'),
        ),
        migrations.AlterField(
            model_name='reshtetahsili',
            name='maghtafkey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pages.maghtaTahsili', verbose_name='انتخاب مقطع تحصیلی'),
        ),
        migrations.AlterField(
            model_name='reshtetahsili',
            name='reshte',
            field=models.CharField(max_length=100, verbose_name='نام رشته'),
        ),
        migrations.AlterField(
            model_name='shahrha',
            name='ostanNamefkey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pages.ostanha', verbose_name='انتخاب استان'),
        ),
        migrations.AlterField(
            model_name='shahrha',
            name='shahrNames',
            field=models.CharField(max_length=100, verbose_name='نام شهر'),
        ),
        migrations.AlterField(
            model_name='sliderimage',
            name='pic',
            field=models.ImageField(upload_to='slider/photos/%y/%m/%d/', verbose_name='عکس های اسلایدر صفحه اول'),
        ),
    ]