from django.contrib import admin
from data.models import (
    RunCategory,
    Activity,
    Record,
    WorkoutStep,
    Lap,
    HeartRateZones,
    LactateThreshold,
)
from data.actions import extract_data  # , extract_lap, extract_workout_set
from datetime import timedelta

# Register your models here.
# admin.site.register(Activity)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    model = Activity
    actions = [extract_data]  # , extract_workout_set, extract_lap]
    list_display = [field.name for field in model._meta.concrete_fields] + [
        "_distance_km",
        "_duration_time",
    ]

    @admin.display(description="Distance (km)")
    def _distance_km(self, obj):
        return round(obj.distance / 1000, 2)

    @admin.display(description="Duration")
    def _duration_time(self, obj):
        return timedelta(seconds=round(obj.duration, 0))


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Record._meta.get_fields()]


@admin.register(RunCategory)
class RunCategoryAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in RunCategory._meta.get_fields()]
    pass


@admin.register(WorkoutStep)
class WorkoutStepdAdmin(admin.ModelAdmin):
    list_display = [field.name for field in WorkoutStep._meta.get_fields()]


@admin.register(Lap)
class LapAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Lap._meta.get_fields()]


@admin.register(HeartRateZones)
class HeartRateZonesAdmin(admin.ModelAdmin):
    model = HeartRateZones
    list_display = [field.name for field in model._meta.concrete_fields]


@admin.register(LactateThreshold)
class LactateThresholdAdmin(admin.ModelAdmin):
    model = LactateThreshold
    list_display = [field.name for field in model._meta.concrete_fields]
