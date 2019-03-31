from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from backend.api.models import Sensor
from django.db.models.query import Q


class IssueListSerializer(ModelSerializer):

    class Meta:
        model = Sensor
        fields = (
            'coords_list',
            'sensor_group',
            'status',
            'temp',
            'wind_direction',
            'wind_speed',
            'humidity',
            'sensor_coords_lat',
            'sensor_coords_lng'
        )

