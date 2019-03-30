from django.db import models
from rest_framework import serializers
from datetime import datetime


class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'pk')

class Sensor(models.Model):
    class Meta:
        verbose_name = 'Датчики'
        verbose_name_plural = 'Датчики'

    status = models.BooleanField(verbose_name='Статус', default=False, blank=False)
    temp = models.IntegerField(verbose_name='Температура', blank=True, null=False)
    wind_direction = models.IntegerField(verbose_name='Направление ветра', blank=True, null=False)
    wind_speed = models.IntegerField(verbose_name='Скорость ветра', blank=True, null=False)
    humidity  = models.IntegerField(verbose_name='Влажность', blank=True, null=False)
    sensor_coords_lat = models.FloatField(verbose_name='Широта', blank=True, null=False)
    sensor_coords_lng = models.FloatField(verbose_name='Долгота', blank=True, null=False)

    def humananized_status(self):
        pass


class Sensor_Data_Set(models.Model):
    class Meta:
        verbose_name = 'Список показателей датчиков'
        verbose_name_plural = 'Список показателей датчиков'

    date_time = models.DateTimeField(default=datetime.now(), blank=True)
    sensor = models.ForeignKey(Sensor,on_delete=models.DO_NOTHING, blank=False, null=False)
    temp = models.IntegerField(verbose_name='Температура', blank=True, null=False)
    wind_direction = models.IntegerField(verbose_name='Направление ветра', blank=True, null=False)
    wind_speed = models.IntegerField(verbose_name='Скорость ветра', blank=True, null=False)
    humidity = models.IntegerField(verbose_name='Влажность', blank=True, null=False)

class Sensor_Area_Point(models.Model):
    class Meta:
        verbose_name = 'Координаты зоны ответственности'
        verbose_name_plural = 'Координаты зоны ответственности'

    point_coords_lat = models.FloatField(verbose_name='Широта', blank=True, null=False)
    point_coords_lng = models.FloatField(verbose_name='Долгота', blank=True, null=False)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, blank=False, null=False)
