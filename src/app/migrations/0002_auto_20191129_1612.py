# Generated by Django 2.2.7 on 2019-11-29 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('expertise', models.CharField(choices=[('General', 'General'), ('Cardiologist', 'Cardiologist')], default='General', max_length=30)),
                ('dr_num', models.IntegerField(unique=True)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RenameField(
            model_name='trackingchart',
            old_name='tests',
            new_name='test',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='id',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='patient',
            name='reg_date',
            field=models.DateTimeField(null=True, verbose_name='Registration Date'),
        ),
        migrations.AddField(
            model_name='trackingchart',
            name='alert_code',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Alert 1', 'Alert 1'), ('Alert 2', 'Alert 2')], default='Pending', max_length=30),
        ),
        migrations.AddField(
            model_name='trackingchart',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='trackingchart',
            name='due_date',
            field=models.DateTimeField(null=True, verbose_name='Time for test to be done by:'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-Mail Address'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='id_num',
            field=models.IntegerField(default=0, primary_key=True, serialize=False, unique=True, verbose_name='ID Number'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Patient First Name'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.IntegerField(verbose_name='Cellphone Number'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='surname',
            field=models.CharField(max_length=30, verbose_name='Patient Last Name'),
        ),
        migrations.AddField(
            model_name='patient',
            name='primary_doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Doctor', verbose_name='Patient Primary Dr.'),
        ),
        migrations.AddField(
            model_name='trackingchart',
            name='ordered_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Doctor'),
        ),
    ]