from data.utils import filter_fitfile, convert_frames
from data.models import Record, WorkoutStep, Lap
import fitdecode
from django.db.models import Min, Max, Avg, Sum
import datetime


def fitfile(file):
    return fitdecode.FitReader(file)


def extract_data(modeladmin, request, queryset):
    for query in queryset:
        if not query.is_file_extracted:
            frames = ["record", "lap", "workout_step"]
            models = [Record, Lap, WorkoutStep]
            filtered_frames = filter_fitfile(query.data_file)
            for frame, model in zip(frames, models):
                frames_list = convert_frames(filtered_frames, frame)
                batch = [model(activity=query, **record) for record in frames_list]
                model.objects.bulk_create(batch)

            activity_records = Record.objects.filter(activity=query)
            query.start_time = activity_records.aggregate(Min("timestamp"))[
                "timestamp__min"
            ]
            query.distance = activity_records.aggregate(Max("distance"))[
                "distance__max"
            ]
            query.heart_rate_avg = int(
                round(
                    activity_records.aggregate(Avg("heart_rate"))["heart_rate__avg"], 0
                )
            )

            activity_laps = Lap.objects.filter(activity=query)

            total_duration = activity_laps.aggregate(Sum("total_timer_time"))[
                "total_timer_time__sum"
            ]

            query.duration = total_duration

            total_calories = activity_laps.aggregate(Sum("total_calories"))[
                "total_calories__sum"
            ]

            query.total_calories = total_calories

            query.is_file_extracted = True
            query.save()
