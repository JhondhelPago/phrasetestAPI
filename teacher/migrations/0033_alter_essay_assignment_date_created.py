# Generated by Django 5.1.1 on 2024-12-28 18:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0032_alter_essay_assignment_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='essay_assignment',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 29, 2, 0, 28, 750534)),
        ),
    ]
