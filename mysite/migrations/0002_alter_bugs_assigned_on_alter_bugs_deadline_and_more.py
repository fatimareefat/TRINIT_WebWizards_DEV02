# Generated by Django 4.0.1 on 2022-01-29 20:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugs',
            name='assigned_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 30, 1, 39, 42, 941335)),
        ),
        migrations.AlterField(
            model_name='bugs',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 30, 1, 39, 42, 941335)),
        ),
        migrations.AlterField(
            model_name='bugs',
            name='resolved_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 30, 1, 39, 42, 941335)),
        ),
    ]
