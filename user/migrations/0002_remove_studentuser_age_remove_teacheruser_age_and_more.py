# Generated by Django 5.1.1 on 2024-10-05 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentuser',
            name='age',
        ),
        migrations.RemoveField(
            model_name='teacheruser',
            name='age',
        ),
        migrations.AlterField(
            model_name='customeuser',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
