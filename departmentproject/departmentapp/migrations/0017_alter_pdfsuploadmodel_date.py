# Generated by Django 4.1 on 2023-05-02 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departmentapp', '0016_pdfsuploadmodel_delete_pdfsupload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdfsuploadmodel',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]