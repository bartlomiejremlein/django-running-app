# Generated by Django 4.2.7 on 2023-11-16 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='accumulated_power',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='activity_type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='cadence',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='distance',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='enhanced_altitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='enhanced_speed',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='fractional_cadence',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='heart_rate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='position_lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='position_long',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='power',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='stance_time',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='stance_time_balance',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='stance_time_percent',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='step_length',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='temperature',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='vertical_oscillation',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='vertical_ratio',
            field=models.FloatField(blank=True, null=True),
        ),
    ]