# Generated by Django 5.1.1 on 2024-11-09 12:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0021_alter_essay_assignment_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='essay_assignment',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2024, 11, 9, 20, 19, 9, 26687)),
        ),
    ]
