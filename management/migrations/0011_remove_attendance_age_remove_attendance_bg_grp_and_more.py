# Generated by Django 4.1.6 on 2023-11-22 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0010_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='Age',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='bg_grp',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='mail_id',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='role',
        ),
    ]
