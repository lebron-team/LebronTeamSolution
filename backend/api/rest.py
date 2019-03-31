from django.http import HttpResponseNotFound, HttpResponse, HttpResponseForbidden, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView, View
from backend.api.models import Area_Point, Sensor, Sensor_Group, Region, Sensor_Data_Set, SensorSerializer, Area_Point_Serializer, GroupSerializer, RegionSerializer, GroupsSerializer, RegionsSerialize, DataSetsSerializer, SensorsSerializer
from django.shortcuts import get_object_or_404
from backend.api import funcs

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
            regions = Region.objects.all()
            data_region = RegionSerializer(regions, many=True)
            return Response({'regions': data_region.data})
        region = Region.objects.get(id=id)
        data_region = RegionSerializer(region)
        return Response({'region': data_region.data})


class Get_Data_Set_By_Sensor_Group(APIView):
    def get(self, requset, id):
        if id == 0:
            groups = Sensor_Group.objects.all()
            data_group = GroupSerializer(groups, many=True)
            return Response({'groups': data_group.data})

        group = Sensor_Group.objects.get(id=id)
        data_group = GroupSerializer(group)
        return  Response({'group': data_group.data})

class Get_Data_Set(APIView):
    def get(self, requset, id, time, time_to):
        if time == 0 and time_to == 0 and id != 0:
            sensor = Sensor.objects.get(id=id)
            data_set = Sensor_Data_Set.objects.filter(sensor=sensor)
            data_data_set = DataSetsSerializer(data_set, many=True)
            return Response({'data_sets': data_data_set.data})
        if id == 0 and time == 0 and time_to == 0:
            print('Всё ноль')
            data_set = Sensor_Data_Set.objects.all()
            data_data_set = DataSetsSerializer(data_set, many=True)
            return Response({'data_sets': data_data_set.data})
        # dj_time = funcs.unix_to_time(time)
        # dj_time_to = funcs.unix_to_time(time_to)
        sensor = Sensor.objects.get(id=id)
        data_set = Sensor_Data_Set.objects.filter(sensor=sensor)
        data_set_out = []
        for x in data_set:
            if x.unix_date <= time_to and x.unix_date >= time:
                data_set_out.append(x)
        data_data_set = DataSetsSerializer(data_set_out, many=True)
        return Response({'data_set': data_data_set.data})

class Get_All_Groups(APIView):
    def get(self, request):
        groups = Sensor_Group.objects.all()
        return Response({'groups': GroupsSerializer(groups, many=True).data})

class Get_All_Regions(APIView):
    def get(self, request):
        regions = Region.objects.all()
        return Response({'regions': RegionsSerialize(regions, many=True).data})

class Get_All_Sensors(APIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        return Response({'sensors': SensorsSerializer(sensors, many=True)})