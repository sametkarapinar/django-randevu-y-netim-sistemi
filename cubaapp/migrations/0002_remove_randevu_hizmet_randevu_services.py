# Generated by Django 5.0 on 2024-05-23 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cubaapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='randevu',
            name='hizmet',
        ),
        migrations.AddField(
            model_name='randevu',
            name='services',
            field=models.JSONField(default=list),
        ),
    ]