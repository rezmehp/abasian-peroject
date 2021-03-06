# Generated by Django 3.0.2 on 2020-11-11 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorialvoice', '0003_voicepics'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursevoice2',
            name='hazineoff',
            field=models.IntegerField(default=1, verbose_name='هزینه با تخفیف به تومان'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coursevoice2',
            name='off_is_published',
            field=models.BooleanField(default=True, verbose_name='تخفیف دارد'),
        ),
    ]
