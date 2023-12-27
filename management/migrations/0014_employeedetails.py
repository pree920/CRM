# Generated by Django 4.1.6 on 2023-11-22 10:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0013_remove_attendance_age_remove_attendance_bg_grp_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employeedetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField(default=0)),
                ('bg_grp', models.CharField(default='default', max_length=4, null=True)),
                ('Age', models.IntegerField(default=0)),
                ('role', models.CharField(default='default', max_length=64, null=True)),
                ('experience', models.CharField(default='default', max_length=15, null=True)),
                ('contact', models.CharField(default='default', max_length=13, null=True)),
                ('mail_id', models.CharField(default='default', max_length=48, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]