# Generated by Django 4.2.7 on 2023-11-17 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_remove_activity_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='duration',
            field=models.FloatField(blank=True, null=True),
        ),
    ]