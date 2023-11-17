# Generated by Django 4.2.7 on 2023-11-17 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_lap_avg_cadence_position_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='distance',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='heart_rate_avg',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='is_file_extracted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='activity',
            name='speed',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lap',
            name='end_position_lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lap',
            name='end_position_long',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lap',
            name='start_position_lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lap',
            name='start_position_long',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
