# Generated by Django 3.1.4 on 2021-02-16 12:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('surname', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=70)),
                ('phone', models.CharField(max_length=11)),
                ('messages', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holiday', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=70)),
                ('notes', models.FileField(upload_to='media')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('batch', models.CharField(choices=[('+2 1st Year', '+2 1st Year'), ('+2 2nd Year', '+2 2nd Year'), ('+3 1st Year', '+3 1st Year'), ('+3 2nd Year', '+3 2nd Year'), ('+3 3rd Year', '+3 3rd Year')], default='+2 1st Year', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], default='1', max_length=20)),
            ],
        ),
    ]
