# Generated by Django 2.2.7 on 2019-11-29 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20191129_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackingchart',
            name='due_date',
            field=models.DateTimeField(null=True, verbose_name='Complete test before:'),
        ),
    ]
