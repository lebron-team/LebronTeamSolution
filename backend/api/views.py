from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.contrib.auth.models import User, Group
from backend.api.models import Sensor
from .models import Message, MessageSerializer
from rest_framework import serializers, viewsets


# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff', 'groups')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class SensorSerializer(serializers.HyperlinkedModelSerializer):
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


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer