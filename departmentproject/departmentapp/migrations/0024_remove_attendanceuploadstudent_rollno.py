# Generated by Django 4.1 on 2023-05-04 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departmentapp', '0023_alter_attendanceuploadstudent_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendanceuploadstudent',
            name='rollno',
        ),
    ]