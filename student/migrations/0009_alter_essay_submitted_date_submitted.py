# Generated by Django 5.1.1 on 2024-11-07 18:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_alter_essay_submitted_date_submitted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='essay_submitted',
            name='date_submitted',
            field=models.DateField(default=datetime.datetime(2024, 11, 8, 2, 4, 27, 68774)),
        ),
    ]
