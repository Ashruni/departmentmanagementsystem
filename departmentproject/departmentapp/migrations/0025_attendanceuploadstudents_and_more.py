# Generated by Django 4.1 on 2023-05-04 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departmentapp', '0024_remove_attendanceuploadstudent_rollno'),
    ]

    operations = [
        migrations.CreateModel(
            name='attendanceuploadstudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('late', 'late'), ('not uploaded', 'not uploaded')], default='not uploaded', max_length=70)),
                ('rollno', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='attendanceuploadstudent',
        ),
    ]
