# Generated by Django 4.1.6 on 2023-11-22 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_alter_attendance_bg_grp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='bg_grp',
            field=models.CharField(default='default', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='contact',
            field=models.CharField(default='default', max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='experience',
            field=models.CharField(default='default', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='mail_id',
            field=models.CharField(default='default', max_length=48, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='role',
            field=models.CharField(default='default', max_length=64, null=True),
        ),
    ]
