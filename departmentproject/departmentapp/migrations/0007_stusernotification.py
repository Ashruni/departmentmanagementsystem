# Generated by Django 4.1 on 2023-04-30 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departmentapp', '0006_rename_semester_departmentsem8assignmentuploadmodel_sid'),
    ]

    operations = [
        migrations.CreateModel(
            name='stusernotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('stnottime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
