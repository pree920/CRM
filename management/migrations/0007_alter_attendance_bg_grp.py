# Generated by Django 4.1.6 on 2023-11-22 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_alter_attendance_bg_grp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='bg_grp',
            field=models.CharField(blank=True, default='default', max_length=4, null=True),
        ),
    ]
