from django.http import HttpResponseNotFound, HttpResponse, HttpResponseForbidden, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView, View
from backend.api.models import Area_Point, Sensor, Sensor_Group, Region, Sensor_Data_Set, SensorSerializer, Area_Point_Serializer
from django.shortcuts import get_object_or_404

class Get_Sensor(APIView):
    def get(self, requst, id):
        sensor = Sensor.objects.get(id=id)
        data_sensor = SensorSerializer(sensor)
        return Response({'sensor': data_sensor.data})

class Get_Data_Set_By_Sensor_Group(APIView):
    def get(self, request, id):
        sensor_group = Sensor_Group.objects.get(id=id)
        sensor_list = Sensor.objects.filter(sensor_group=sensor_group.id)
        coords_list = Area_Point.objects.filter(points_list=sensor_group.coords_list)
        return JsonResponse({'sensor_list': sensor_list, 'coords_list': coords_list})

class Get_Data_Set_By_Region(APIView):
    def get(self, requset, id):
        group = Sensor_Group.objects.get(id)
        sensors = Sensor.objects.filter(sensor_group=group)
        group_points = Area_Point.objects.filter(points_list=group.coords_list)
        # data_sensors =
        pass



