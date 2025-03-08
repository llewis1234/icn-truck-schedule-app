from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from schedules.views import TruckScheduleViewSet, schedule_by_origin_destination, unique_origins_destinations

# Setup Django REST Framework router
router = DefaultRouter()
router.register(r'truckschedule', TruckScheduleViewSet)

# Serve the front-end HTML page
def home(request):
    return render(request, "index.html")  # Updated to load the front-end template

urlpatterns = [
    path('', home),  # Serves the front-end page
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/schedule/<str:origin>/<str:destination>/', schedule_by_origin_destination),
    path('api/origins-destinations/', unique_origins_destinations),  # New API route for dropdowns
]