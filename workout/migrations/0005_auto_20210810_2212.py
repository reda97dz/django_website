# Generated by Django 3.0.14 on 2021-08-10 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0004_auto_20210810_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='activity',
            field=models.CharField(choices=[('run', 'Run'), ('hike', 'Hike')], default='run', max_length=20),
        ),
        migrations.AlterField(
            model_name='run',
            name='date',
            field=models.DateField(),
        ),
    ]
