# Generated by Django 4.2 on 2023-04-29 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departmentapp', '0003_semsubjectsuploadother_delete_semsubjectuploadother'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentregistrationmodel',
            name='studentimage',
            field=models.ImageField(upload_to='departmentapp/static'),
        ),
    ]