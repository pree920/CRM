# Generated by Django 4.1.6 on 2023-11-22 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_alter_attendance_bg_grp_alter_attendance_contact_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Attendance',
        ),
    ]