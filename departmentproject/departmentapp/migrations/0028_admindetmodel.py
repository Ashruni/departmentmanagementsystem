# Generated by Django 4.1 on 2023-05-07 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departmentapp', '0027_alter_attendanceuploadstudents_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='admindetmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('dep', models.CharField(max_length=20)),
            ],
        ),
    ]