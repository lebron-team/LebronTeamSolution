from django.http import HttpResponseNotFound, HttpResponse, HttpResponseForbidden, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView, View
from backend.api.models import Sensor_Area_Point, Sensor, Sensor_Data_Set
from django.shortcuts import get_object_or_404


class Get_Sensor_Data(APIView):
    def get(self, requst, id):
        sensor = Sensor.objects.get(id=id)
