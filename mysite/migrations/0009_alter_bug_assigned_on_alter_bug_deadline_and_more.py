# Generated by Django 4.0.1 on 2022-01-30 04:11

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_alter_bug_assigned_on_alter_bug_deadline_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='assigned_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 30, 9, 41, 29, 669483), null=True),
        ),
        migrations.AlterField(
            model_name='bug',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 30, 9, 41, 29, 669483)),
        ),
        migrations.AlterField(
            model_name='bug',
            name='resolved_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 30, 9, 41, 29, 669483)),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='role',
            field=models.CharField(choices=[('OL', 'Organisation-Lead'), ('SDE1', 'SeniorDeveloper'), ('SDE2', 'JuniorDeveloper'), ('U', 'User')], default='U', max_length=4),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('bug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bug', to='mysite.bug')),
            ],
        ),
    ]
