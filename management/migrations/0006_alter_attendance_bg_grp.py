# Generated by Django 4.1.6 on 2023-11-22 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_alter_attendance_bg_grp_alter_attendance_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='bg_grp',
            field=models.CharField(default='default', max_length=4, null=True),
        ),
    ]