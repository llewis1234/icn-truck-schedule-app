from rest_framework import serializers, viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import TruckSchedule

class TruckScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TruckSchedule
        fields = '__all__'

class TruckScheduleViewSet(viewsets.ModelViewSet):
    queryset = TruckSchedule.objects.all()
    serializer_class = TruckScheduleSerializer

@api_view(['GET'])
def schedule_by_origin_destination(request, origin, destination):
    schedules = TruckSchedule.objects.filter(origin=origin, destination=destination)
    serializer = TruckScheduleSerializer(schedules, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def unique_origins_destinations(request):
    origins = TruckSchedule.objects.values_list('origin', flat=True).distinct()
    destinations = TruckSchedule.objects.values_list('destination', flat=True).distinct()
    return Response({'origins': list(origins), 'destinations': list(destinations)})