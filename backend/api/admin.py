from django.contrib import admin
from backend.api.models import Sensor, Area_Point, Sensor_Data_Set, Alarm_Status, Area_Points_List, Region, Sensor_Group
# Register your models here.

admin.site.register(Sensor)
admin.site.register(Area_Point)
admin.site.register(Alarm_Status)
admin.site.register(Area_Points_List)
admin.site.register(Region)
admin.site.register(Sensor_Data_Set)
admin.site.register(Sensor_Group)
