# Generated by Django 3.0.2 on 2020-11-11 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0016_auto_20200910_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseexam2',
            name='hazineoff',
            field=models.IntegerField(default=0, verbose_name='هزینه با تخفیف به تومان'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='courseexam2',
            name='off_is_published',
            field=models.BooleanField(default=True, verbose_name='تخفیف دارد'),
        ),
    ]
