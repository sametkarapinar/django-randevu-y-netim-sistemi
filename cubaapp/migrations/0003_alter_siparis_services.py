# Generated by Django 5.0 on 2024-05-23 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cubaapp', '0002_remove_randevu_hizmet_randevu_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siparis',
            name='services',
            field=models.JSONField(default=list),
        ),
    ]