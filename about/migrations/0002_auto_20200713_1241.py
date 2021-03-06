# Generated by Django 3.0.2 on 2020-07-13 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutadmin',
            options={'verbose_name_plural': 'تنظیمات صفحه درباره ما'},
        ),
        migrations.AlterField(
            model_name='aboutadmin',
            name='modir1_email',
            field=models.EmailField(max_length=300, verbose_name='ایمیل مدیر 1'),
        ),
        migrations.AlterField(
            model_name='aboutadmin',
            name='modir1_name',
            field=models.CharField(max_length=300, verbose_name='نام و نام خانوادگی مدیر 1'),
        ),
        migrations.AlterField(
            model_name='aboutadmin',
            name='modir1_pic',
            field=models.ImageField(upload_to='about/photos/%y/%m/%d/', verbose_name='عکس مدیر 1'),
        ),
        migrations.AlterField(
            model_name='aboutadmin',
            name='modir1_semat',
            field=models.CharField(max_length=300, verbose_name='سمت مدیر 1'),
        ),
        migrations.AlterField(
            model_name='aboutadmin',
            name='modir1_text',
            field=models.TextField(verbose_name='توضیحات درباره مدیر 1'),
        ),
        migrations.AlterField(
            model_name='aboutadmin',
            name='modir2_email',
            field=models.EmailField(max_length=300, verbose_name='ایمیل مدیر 2'),
        ),
        migrations.AlterField(
            model_name='aboutadmin',
            name='modir2_name',
            field=models.CharField(max_length=300, verbose_name='نام و نام خانوادگی مدیر 2'),
        ),
        migrations.AlterField(
            model_name='aboutadmin',
            name='modir2_pic',
            field=models.ImageField(upload_to='about/photos/%y/%m/%d/', verbose_name='عکس مدیر 2'),
        ),
        migrations.AlterField(
            model_name='aboutadmin',
            name='modir2_semat',
            field=models.CharField(max_length=300, verbose_name='سمت مدیر 2'),
        ),
        migrations.AlterField(
            model_name='aboutadmin',
            name='modir2_text',
            field=models.TextField(verbose_name='توضیحات درباره مدیر 2'),
        ),
        migrations.AlterField(
            model_name='aboutadmin',
            name='modir3_email',
            field=models.EmailField(max_length=300, verbose_name='ایمیل مدیر 3'),
        ),
        migrations.AlterField(
            model_name='aboutadmin',
            name='modir3_name',
            field=models.CharField(max_length=300, verbose_name='نام و نام خانوادگی مدیر 3'),
        ),
        migrations.AlterField(
            model_name='aboutadmin',
            name='modir3_pic',
            field=models.ImageField(upload_to='about/photos/%y/%m/%d/', verbose_name='عکس مدیر 3'),
        ),
        migrations.AlterField(
            model_name='aboutadmin',
            name='modir3_semat',
            field=models.CharField(max_length=300, verbose_name='سمت مدیر 3'),
        ),
        migrations.AlterField(
            model_name='aboutadmin',
            name='modir3_text',
            field=models.TextField(verbose_name='توضیحات درباره مدیر 3'),
        ),
        migrations.AlterField(
            model_name='aboutadmin',
            name='pic',
            field=models.ImageField(upload_to='contact/photos/%y/%m/%d/', verbose_name='عکس بالای صفحه'),
        ),
        migrations.AlterField(
            model_name='aboutadmin',
            name='pic1',
            field=models.ImageField(upload_to='about/photos/%y/%m/%d/', verbose_name='عکس شماره 1'),
        ),
        migrations.AlterField(
            model_name='aboutadmin',
            name='pic2',
            field=models.ImageField(upload_to='about/photos/%y/%m/%d/', verbose_name='عکس شماره 2'),
        ),
        migrations.AlterField(
            model_name='aboutadmin',
            name='pic3',
            field=models.ImageField(upload_to='about/photos/%y/%m/%d/', verbose_name='عکس شماره 3'),
        ),
        migrations.AlterField(
            model_name='aboutadmin',
            name='pic4',
            field=models.ImageField(upload_to='about/photos/%y/%m/%d/', verbose_name='عکس شماره 4'),
        ),
        migrations.AlterField(
            model_name='aboutadmin',
            name='pic5',
            field=models.ImageField(upload_to='about/photos/%y/%m/%d/', verbose_name='عکس شماره 5'),
        ),
        migrations.AlterField(
            model_name='aboutadmin',
            name='pic6',
            field=models.ImageField(upload_to='about/photos/%y/%m/%d/', verbose_name='عکس شماره 6'),
        ),
        migrations.AlterField(
            model_name='aboutadmin',
            name='pic7',
            field=models.ImageField(upload_to='about/photos/%y/%m/%d/', verbose_name='عکس شماره 7'),
        ),
        migrations.AlterField(
            model_name='aboutadmin',
            name='pic8',
            field=models.ImageField(upload_to='about/photos/%y/%m/%d/', verbose_name='عکس شماره 8'),
        ),
        migrations.AlterField(
            model_name='aboutadmin',
            name='pic_is_publish',
            field=models.BooleanField(default=True, verbose_name='نمایش یا عدم نمایش عکس های محیط شرکت'),
        ),
        migrations.AlterField(
            model_name='aboutadmin',
            name='pic_title',
            field=models.CharField(max_length=500, verbose_name='تیتر عکس های محیط شرکت'),
        ),
        migrations.AlterField(
            model_name='aboutadmin',
            name='text_about',
            field=models.TextField(blank=True, verbose_name='توضیحات شرکت'),
        ),
        migrations.AlterField(
            model_name='aboutadmin',
            name='title_page',
            field=models.CharField(max_length=500, verbose_name='تیتر صفحه'),
        ),
        migrations.AlterField(
            model_name='aboutadmin',
            name='title_text',
            field=models.CharField(max_length=500, verbose_name='تیتر توضیحات شرکت'),
        ),
    ]
