# Generated by Django 4.2.7 on 2023-11-17 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_activity_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='duration',
        ),
    ]
