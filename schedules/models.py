from django.db import models

class TruckSchedule(models.Model):
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    load_day = models.CharField(max_length=20)
    load_start_time = models.TimeField()
    load_complete_time = models.TimeField()
    depart_day = models.CharField(max_length=20)
    depart_time = models.TimeField()
    arrive_day = models.CharField(max_length=20)
    arrive_time = models.TimeField()
    unload_day = models.CharField(max_length=20)
    unload_time = models.TimeField()
    transit_time = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.origin} to {self.destination} ({self.load_day})"
