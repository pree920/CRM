# Generated by Django 4.1.6 on 2023-11-22 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_alter_attendance_entry_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='Age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='attendance',
            name='bg_grp',
            field=models.CharField(default=None, max_length=4),
        ),
        migrations.AddField(
            model_name='attendance',
            name='contact',
            field=models.CharField(default=None, max_length=13),
        ),
        migrations.AddField(
            model_name='attendance',
            name='emp_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='attendance',
            name='experience',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AddField(
            model_name='attendance',
            name='mail_id',
            field=models.CharField(default=None, max_length=48),
        ),
        migrations.AddField(
            model_name='attendance',
            name='role',
            field=models.CharField(default=None, max_length=64),
        ),
    ]
