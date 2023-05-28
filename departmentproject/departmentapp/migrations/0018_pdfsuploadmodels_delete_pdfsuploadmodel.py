# Generated by Django 4.1 on 2023-05-03 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departmentapp', '0017_alter_pdfsuploadmodel_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='pdfsuploadmodels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=50)),
                ('pdfs', models.FileField(upload_to='departmentapp/static')),
                ('date', models.DateField(auto_now_add=True)),
                ('sem', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='pdfsuploadmodel',
        ),
    ]
