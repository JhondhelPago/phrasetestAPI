# Generated by Django 5.1.1 on 2024-11-03 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_customuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentuser',
            name='section',
            field=models.CharField(blank=True, max_length=8),
        ),
    ]
