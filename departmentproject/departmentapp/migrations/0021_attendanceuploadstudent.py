# Generated by Django 4.1 on 2023-05-03 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departmentapp', '0020_alter_pdfsuploadmodels_pdfs'),
    ]

    operations = [
        migrations.CreateModel(
            name='attendanceuploadstudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(max_length=30)),
                ('rollno', models.CharField(max_length=30)),
            ],
        ),
    ]