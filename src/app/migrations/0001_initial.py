# Generated by Django 2.2.7 on 2019-11-28 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('id_num', models.IntegerField(unique=True)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('test_num', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TrackingChart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Patient')),
                ('tests', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Test')),
            ],
        ),
    ]
