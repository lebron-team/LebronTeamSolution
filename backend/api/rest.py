from django.http import HttpResponseNotFound, HttpResponse, HttpResponseForbidden, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView, View
from backend.api.models import Area_Point, Sensor, Sensor_Group, Region, Sensor_Data_Set
from django.shortcuts import get_object_or_404


class Get_Sensor(APIView):
    def get(self, requst, id):
        sensor = Sensor.objects.get(id=id)
        return Response({'sensor': sensor})


class Get_Data_Set_By_Sensor_Group(APIView):
    def get(self, request, id):
        sensor_group = Sensor_Group.objects.get(id=id)
        return Response()

class Get_Data_Set_By_Region(APIView):
    def get(self, requset):
        pass

