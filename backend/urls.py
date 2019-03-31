"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from backend.api.models import Sensor

from .api.views import index_view, MessageViewSet, UserViewSet, GroupViewSet, SensorViewSet
from backend.api import rest

router = routers.DefaultRouter()
router.register('messages', MessageViewSet)

user_router = routers.DefaultRouter()
user_router.register('users', UserViewSet)

group_router = routers.DefaultRouter()
group_router.register('groups', GroupViewSet)

sensor_router = routers.DefaultRouter()
sensor_router.register('sensors', SensorViewSet)


urlpatterns = [

    # http://localhost:8000/
    path('', index_view, name='index'),

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    path('api-out/', include(user_router.urls)),

    path('api-out/', include(group_router.urls)),

    # http://localhost:8000/api/admin/
    path('api/admin/', admin.site.urls),

    path('api/sensor/', include(sensor_router.urls)),

    path('api/rest/sensor/<int:id>/', rest.Get_Sensor.as_view()),
    path('api/rest/group/<int:id>/', rest.Get_Data_Set_By_Region.as_view()),
]



