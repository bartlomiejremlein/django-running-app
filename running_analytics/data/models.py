from django.db import models


class RunCategory(models.Model):
    name = models.CharField(max_length=50)


# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=200, null=False)
    category = models.ForeignKey(to=RunCategory, on_delete=models.CASCADE)
    data_file = models.FileField()


class Record(models.Model):
    activity = models.ForeignKey(to=Activity, on_delete=models.CASCADE)


class Lap(models.Model):
    activity = models.ForeignKey(to=Activity, on_delete=models.CASCADE)


class WorkoutStep(models.Model):
    activity = models.ForeignKey(to=Activity, on_delete=models.CASCADE)
