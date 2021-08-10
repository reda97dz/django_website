# Generated by Django 3.0.14 on 2021-08-10 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('distance', models.FloatField()),
                ('duration', models.FloatField()),
                ('pace', models.FloatField()),
                ('date', models.DateTimeField()),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]
