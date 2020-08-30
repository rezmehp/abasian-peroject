# Generated by Django 3.0.2 on 2020-07-13 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20200713_1241'),
        ('tutorialapplication', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='applications',
            options={'verbose_name_plural': 'فایل ها'},
        ),
        migrations.AlterModelOptions(
            name='courseapplication2',
            options={'verbose_name_plural': 'نرم افزارها'},
        ),
        migrations.AlterModelOptions(
            name='tutorialapplicationadmin',
            options={'verbose_name_plural': 'تنظیمات صفحه'},
        ),
        migrations.AlterField(
            model_name='applications',
            name='applicationapplication',
            field=models.FileField(blank=True, upload_to='courseapplication/applications/%y/%m/%d/', verbose_name='فایل'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='applicationapplication_is_published',
            field=models.BooleanField(default=True, verbose_name='پابلیش فایل'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='applicationlink',
            field=models.CharField(blank=True, max_length=1000, verbose_name='لینک فایل'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='applicationlink_is_published',
            field=models.BooleanField(default=True, verbose_name='پابلیش لینک فایل'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='applicationname',
            field=models.CharField(max_length=1000, verbose_name='نام فایل'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='coursenamefkey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tutorialapplication.courseapplication2', verbose_name='نام نرم افزار'),
        ),
        migrations.AlterField(
            model_name='courseapplication2',
            name='coursename',
            field=models.CharField(max_length=1000, verbose_name='نام نرم افزار'),
        ),
        migrations.AlterField(
            model_name='courseapplication2',
            name='hazine',
            field=models.IntegerField(verbose_name='هزینه به ریال'),
        ),
        migrations.AlterField(
            model_name='courseapplication2',
            name='maghtafkey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pages.maghtaTahsili', verbose_name='مقطع'),
        ),
        migrations.AlterField(
            model_name='courseapplication2',
            name='modaresinfkey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pages.modaresin', verbose_name='نام سازنده'),
        ),
        migrations.AlterField(
            model_name='courseapplication2',
            name='pic',
            field=models.ImageField(upload_to='courseapplication/photos/%y/%m/%d/', verbose_name='فایل عکس'),
        ),
        migrations.AlterField(
            model_name='courseapplication2',
            name='reshteTahsilifkey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pages.reshteTahsili', verbose_name='رشته'),
        ),
        migrations.AlterField(
            model_name='courseapplication2',
            name='saattadris',
            field=models.CharField(max_length=1000, verbose_name='زمان نزم افزار'),
        ),
        migrations.AlterField(
            model_name='courseapplication2',
            name='tozihat',
            field=models.TextField(verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='tutorialapplicationadmin',
            name='pic',
            field=models.ImageField(upload_to='tutorialapplication/photos/%y/%m/%d/', verbose_name='عکس بالای صفحه'),
        ),
        migrations.AlterField(
            model_name='tutorialapplicationadmin',
            name='text_click',
            field=models.CharField(max_length=500, verbose_name='تیتر دکمه سرچ'),
        ),
        migrations.AlterField(
            model_name='tutorialapplicationadmin',
            name='title_1',
            field=models.CharField(max_length=500, verbose_name='تیتر اول، فایل های پیشنهادی'),
        ),
        migrations.AlterField(
            model_name='tutorialapplicationadmin',
            name='title_2',
            field=models.CharField(max_length=500, verbose_name='تیتر دوم، جدیدترین فایل ها'),
        ),
        migrations.AlterField(
            model_name='tutorialapplicationadmin',
            name='title_page',
            field=models.CharField(max_length=500, verbose_name='تیتر صفحه'),
        ),
        migrations.AlterField(
            model_name='tutorialapplicationadmin',
            name='title_search',
            field=models.CharField(max_length=500, verbose_name='تیتر قسمت سرچ'),
        ),
    ]