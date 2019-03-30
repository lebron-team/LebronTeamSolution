from django.http import HttpResponseNotFound, HttpResponse, HttpResponseForbidden, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView, View
from backend.api.models import Area_Point, Sensor
from django.shortcuts import get_object_or_404


class Area_Load(APIView):
    def get(self, requst, id):
        sensor = Sensor.objects.get(id=id)
        area_points = Area_Point.objects.filter(sensor=sensor)
        return Response({'sensor': sensor, 'area_points': area_points})


class Get_Data_Set(APIView):
    def get(self, request):
        pass