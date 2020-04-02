# Generated by Django 3.0.2 on 2020-03-30 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contact', '0002_auto_20200320_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactuserpayam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soal', models.TextField(blank=True)),
                ('tarikhjavab', models.CharField(max_length=200)),
                ('javabadmin', models.TextField(blank=True)),
                ('usernamefkey', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]