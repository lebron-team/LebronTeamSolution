from django.http import HttpResponseNotFound, HttpResponse, HttpResponseForbidden, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView, View
from backend.api.models import Area_Point, Sensor, Sensor_Group, Region, Sensor_Data_Set, SensorSerializer, Area_Point_Serializer, GroupSerializer
from django.shortcuts import get_object_or_404

class Get_Sensor(APIView):
    def get(self, requst, id):
        if id == 0:
            sensor = Sensor.objects.all()
            data_sensor = SensorSerializer(sensor, many=True)
            return Response(data_sensor.data)
        sensor = Sensor.objects.get(id=id)
        data_sensor = SensorSerializer(sensor)
        return Response({'sensor': data_sensor.data})

class Get_Data_Set_By_Region(APIView):
    def get(self, requset, id):
        if id == 0:
            pass
        pass


class Get_Data_Set_By_Sensor_Group(APIView):
    def get(self, requset, id):
        if id == 0:
            groups = Sensor_Group.objects.all()
            data_group = GroupSerializer(groups, many=True)
            return Response({'groups': data_group.data})

        group = Sensor_Group.objects.get(id=id)
        data_group = GroupSerializer(group)
        return  Response({'group': data_group.data})


