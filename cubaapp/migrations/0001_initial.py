# Generated by Django 5.0 on 2024-05-23 20:30

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hizmet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Musteri',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('birthdate', models.DateField()),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Siparis',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.CharField(max_length=100)),
                ('services', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateTimeField()),
                ('price', models.FloatField()),
                ('debt', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Yontem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Randevu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('status', models.BooleanField(default=False)),
                ('note', models.TextField()),
                ('hizmet', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='cubaapp.hizmet')),
            ],
        ),
        migrations.CreateModel(
            name='Odeme',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('amount', models.FloatField()),
                ('note', models.TextField()),
                ('method', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='cubaapp.yontem')),
            ],
        ),
    ]
