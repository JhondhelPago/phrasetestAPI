# Generated by Django 5.1.1 on 2024-11-04 06:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0015_alter_essay_assignment_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='essay_assignment',
            name='assignment_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='essay_assignment',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2024, 11, 4, 14, 51, 53, 514788)),
        ),
    ]
