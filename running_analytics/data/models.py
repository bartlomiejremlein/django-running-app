from django.db import models


class RunCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=200, null=False)
    category = models.ForeignKey(to=RunCategory, on_delete=models.CASCADE)
    data_file = models.FileField()
    is_file_extracted = models.BooleanField(default=False)
    start_time = models.DateTimeField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    heart_rate_avg = models.PositiveSmallIntegerField(blank=True, null=True)
    total_calories = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.duration and self.distance:
            self.speed = round(self.distance / self.duration * 3.6, 2)  ## M/S to KM/H
        super(Activity, self).save(*args, **kwargs)


class Record(models.Model):
    activity = models.ForeignKey(to=Activity, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(blank=True, null=True)
    position_lat = models.FloatField(blank=True, null=True)
    position_long = models.FloatField(blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    accumulated_power = models.IntegerField(blank=True, null=True)
    enhanced_speed = models.FloatField(blank=True, null=True)
    enhanced_altitude = models.FloatField(blank=True, null=True)
    power = models.SmallIntegerField(blank=True, null=True)
    vertical_oscillation = models.FloatField(blank=True, null=True)
    stance_time_percent = models.FloatField(blank=True, null=True)
    stance_time = models.FloatField(blank=True, null=True)
    vertical_ratio = models.FloatField(blank=True, null=True)
    stance_time_balance = models.FloatField(blank=True, null=True)
    step_length = models.FloatField(blank=True, null=True)
    heart_rate = models.IntegerField(blank=True, null=True)
    cadence = models.IntegerField(blank=True, null=True)
    temperature = models.IntegerField(blank=True, null=True)
    activity_type = models.CharField(max_length=50, blank=True, null=True)
    fractional_cadence = models.FloatField(blank=True, null=True)


class Lap(models.Model):
    activity = models.ForeignKey(to=Activity, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    start_position_lat = models.FloatField(blank=True, null=True)
    start_position_long = models.FloatField(blank=True, null=True)
    end_position_lat = models.FloatField(blank=True, null=True)
    end_position_long = models.FloatField(blank=True, null=True)
    total_elapsed_time = models.FloatField(blank=True, null=True)
    total_timer_time = models.FloatField(blank=True, null=True)
    total_distance = models.FloatField(blank=True, null=True)
    total_strides = models.IntegerField(blank=True, null=True)
    total_work = models.IntegerField(blank=True, null=True)
    time_standing = models.CharField(max_length=100, blank=True, null=True)
    avg_left_power_phase = models.CharField(max_length=100, blank=True, null=True)
    avg_left_power_phase_peak = models.CharField(max_length=100, blank=True, null=True)
    avg_right_power_phase = models.CharField(max_length=100, blank=True, null=True)
    avg_right_power_phase_peak = models.CharField(max_length=100, blank=True, null=True)
    avg_power_position = models.CharField(max_length=100, blank=True, null=True)
    max_power_position = models.CharField(max_length=100, blank=True, null=True)
    enhanced_avg_speed = models.FloatField(blank=True, null=True)
    enhanced_max_speed = models.FloatField(blank=True, null=True)
    enhanced_avg_altitude = models.CharField(max_length=100, blank=True, null=True)
    enhanced_min_altitude = models.FloatField(blank=True, null=True)
    enhanced_max_altitude = models.FloatField(blank=True, null=True)
    total_grit = models.CharField(max_length=100, blank=True, null=True)
    avg_flow = models.CharField(max_length=100, blank=True, null=True)
    message_index = models.IntegerField(blank=True, null=True)
    total_calories = models.IntegerField(blank=True, null=True)
    total_fat_calories = models.CharField(max_length=100, blank=True, null=True)
    avg_power = models.IntegerField(blank=True, null=True)
    max_power = models.IntegerField(blank=True, null=True)
    total_ascent = models.IntegerField(blank=True, null=True)
    total_descent = models.IntegerField(blank=True, null=True)
    num_lengths = models.CharField(max_length=100, blank=True, null=True)
    normalized_power = models.IntegerField(blank=True, null=True)
    left_right_balance = models.CharField(max_length=100, blank=True, null=True)
    first_length_index = models.CharField(max_length=100, blank=True, null=True)
    avg_stroke_distance = models.CharField(max_length=100, blank=True, null=True)
    num_active_lengths = models.CharField(max_length=100, blank=True, null=True)
    wkt_step_index = models.CharField(max_length=100, blank=True, null=True)
    avg_vertical_oscillation = models.FloatField(blank=True, null=True)
    avg_stance_time_percent = models.FloatField(blank=True, null=True)
    avg_stance_time = models.FloatField(blank=True, null=True)
    stand_count = models.CharField(max_length=100, blank=True, null=True)
    avg_vertical_ratio = models.FloatField(blank=True, null=True)
    avg_stance_time_balance = models.FloatField(blank=True, null=True)
    avg_step_length = models.FloatField(blank=True, null=True)
    event = models.CharField(max_length=100, blank=True, null=True)
    event_type = models.CharField(max_length=100, blank=True, null=True)
    avg_heart_rate = models.IntegerField(blank=True, null=True)
    max_heart_rate = models.IntegerField(blank=True, null=True)
    avg_running_cadence = models.IntegerField(blank=True, null=True)
    max_running_cadence = models.IntegerField(blank=True, null=True)
    intensity = models.CharField(max_length=100, blank=True, null=True)
    lap_trigger = models.CharField(max_length=100, blank=True, null=True)
    sport = models.CharField(max_length=100, blank=True, null=True)
    event_group = models.CharField(max_length=100, blank=True, null=True)
    swim_stroke = models.CharField(max_length=100, blank=True, null=True)
    sub_sport = models.CharField(max_length=100, blank=True, null=True)
    avg_temperature = models.IntegerField(blank=True, null=True)
    max_temperature = models.IntegerField(blank=True, null=True)
    avg_fractional_cadence = models.FloatField(blank=True, null=True)
    max_fractional_cadence = models.FloatField(blank=True, null=True)
    total_fractional_cycles = models.CharField(max_length=100, blank=True, null=True)
    avg_left_torque_effectiveness = models.CharField(
        max_length=100, blank=True, null=True
    )
    avg_right_torque_effectiveness = models.CharField(
        max_length=100, blank=True, null=True
    )
    avg_left_pedal_smoothness = models.CharField(max_length=100, blank=True, null=True)
    avg_right_pedal_smoothness = models.CharField(max_length=100, blank=True, null=True)
    avg_combined_pedal_smoothness = models.CharField(
        max_length=100, blank=True, null=True
    )
    avg_left_pco = models.CharField(max_length=100, blank=True, null=True)
    avg_right_pco = models.CharField(max_length=100, blank=True, null=True)
    avg_cadence_position = models.CharField(max_length=100, blank=True, null=True)
    max_cadence_position = models.CharField(max_length=100, blank=True, null=True)
    total_fractional_ascent = models.FloatField(blank=True, null=True)
    total_fractional_descent = models.FloatField(blank=True, null=True)


class WorkoutStep(models.Model):
    activity = models.ForeignKey(to=Activity, on_delete=models.CASCADE)
    wkt_step_name = models.CharField(max_length=100, blank=True, null=True)
    duration_time = models.FloatField(blank=True, null=True)
    target_hr_zone = models.IntegerField(blank=True, null=True)
    custom_target_heart_rate_low = models.IntegerField(blank=True, null=True)
    custom_target_heart_rate_high = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=100, blank=True, null=True)
    message_index = models.IntegerField(blank=True, null=True)
    exercise_category = models.CharField(max_length=100, blank=True, null=True)
    exercise_name = models.CharField(max_length=100, blank=True, null=True)
    exercise_weight = models.CharField(max_length=100, blank=True, null=True)
    weight_display_unit = models.CharField(max_length=100, blank=True, null=True)
    duration_type = models.CharField(max_length=100, blank=True, null=True)
    target_type = models.CharField(max_length=100, blank=True, null=True)
    intensity = models.CharField(max_length=100, blank=True, null=True)
    equipment = models.CharField(max_length=100, blank=True, null=True)


class HeartRateZones(models.Model):
    date = models.DateField(blank=True, null=True)
    zone_1 = models.PositiveSmallIntegerField(blank=True, null=True)
    zone_2 = models.PositiveSmallIntegerField(blank=True, null=True)
    zone_3 = models.PositiveSmallIntegerField(blank=True, null=True)
    zone_4 = models.PositiveSmallIntegerField(blank=True, null=True)
    zone_5 = models.PositiveSmallIntegerField(blank=True, null=True)


class LactateThreshold(models.Model):
    date = models.DateField(blank=True, null=True)
    pace = models.PositiveSmallIntegerField(blank=True, null=True)
    heart_rate = models.PositiveSmallIntegerField(blank=True, null=True)
