# Generated by Django 4.1 on 2023-05-02 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departmentapp', '0013_alter_departmentsem8assignmentuploadmodel_assignmentm1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departmentsemmarkupload',
            name='semester',
            field=models.IntegerField(default='-'),
        ),
        migrations.AlterField(
            model_name='departmentsemmarkupload',
            name='suba',
            field=models.IntegerField(default='-'),
        ),
        migrations.AlterField(
            model_name='departmentsemmarkupload',
            name='subb',
            field=models.IntegerField(default='-'),
        ),
        migrations.AlterField(
            model_name='departmentsemmarkupload',
            name='subc',
            field=models.IntegerField(default='-'),
        ),
        migrations.AlterField(
            model_name='departmentsemmarkupload',
            name='subd',
            field=models.IntegerField(default='-'),
        ),
        migrations.AlterField(
            model_name='internals',
            name='pp1',
            field=models.IntegerField(default='-'),
        ),
        migrations.AlterField(
            model_name='internals',
            name='pp2',
            field=models.IntegerField(default='-'),
        ),
        migrations.AlterField(
            model_name='internals',
            name='pp3',
            field=models.IntegerField(default='-'),
        ),
        migrations.AlterField(
            model_name='internals',
            name='pp4',
            field=models.IntegerField(default='-'),
        ),
    ]