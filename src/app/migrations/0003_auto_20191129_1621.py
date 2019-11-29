# Generated by Django 2.2.7 on 2019-11-29 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191129_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='dr_num',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='id',
        ),
        migrations.RemoveField(
            model_name='test',
            name='id',
        ),
        migrations.RemoveField(
            model_name='test',
            name='test_num',
        ),
        migrations.AddField(
            model_name='doctor',
            name='license_num',
            field=models.IntegerField(default=0, primary_key=True, serialize=False, unique=True, verbose_name='Dr. Medical License'),
        ),
        migrations.AddField(
            model_name='test',
            name='code',
            field=models.IntegerField(default=0, primary_key=True, serialize=False, unique=True, verbose_name='Test Code'),
        ),
    ]
