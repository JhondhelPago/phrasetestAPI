# Generated by Django 5.1.1 on 2024-11-01 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_section_teacher_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='section_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
