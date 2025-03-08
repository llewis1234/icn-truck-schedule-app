from django.contrib import admin
from .models import TruckSchedule

@admin.register(TruckSchedule)
class TruckScheduleAdmin(admin.ModelAdmin):
    list_display = ('origin', 'destination', 'load_day', 'depart_day', 'arrive_day')
    search_fields = ('origin', 'destination', 'load_day')

