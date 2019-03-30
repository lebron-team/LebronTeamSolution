from django.contrib import admin
from backend.api.models import Sensor, Sensor_Area_Point, Sensor_Data_Set
# Register your models here.

admin.site.register(Sensor)
admin.site.register(Sensor_Area_Point)
admin.site.register(Sensor_Data_Set)
