from django.db import models
from rest_framework import serializers
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework.serializers import ModelSerializer

class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'pk')

class Area_Points_List(models.Model):
    class Meta:
        verbose_name = 'Список координат'
        verbose_name_plural = 'Список координат'


    def humananized_status(self):
        pass

class Alarm_Status(models.Model):
    class Meta:
        verbose_name = 'Тревожный статус'
        verbose_name_plural = 'Тревожный статус'

    name = models.CharField(verbose_name='Имя статуса', max_length=30)
    status_text = models.CharField(verbose_name='Текст статуса', max_length=60)

class Area_Point(models.Model):
    class Meta:
        verbose_name = 'Координатa'
        verbose_name_plural = 'Координатa'

    point_coords_lat = models.DecimalField(verbose_name='Широта', blank=True, null=False, max_digits=10, decimal_places=6)
    point_coords_lng = models.DecimalField(verbose_name='Долгота', blank=True, null=False, max_digits=10, decimal_places=6)
    points_list = models.ForeignKey(Area_Points_List, on_delete=models.CASCADE, blank=False, null=False)
    array_number = models.IntegerField(verbose_name='Порядковый номер', blank=True, null=False)

class Region(models.Model):
    class Meta:
        verbose_name = 'Область'
        verbose_name_plural = 'Область'

    coords_list = models.ForeignKey(Area_Points_List, verbose_name='Список координат', on_delete=models.DO_NOTHING, blank=True,
                                    null=True)
    name = models.CharField(verbose_name='Имя области', max_length=20)

class Sensor_Group(models.Model):
    class Meta:
        verbose_name = 'Координаты зоны ответственности группы датчиков'
        verbose_name_plural = 'Координаты зоны ответственности группы датчиков'

    coords_list = models.ForeignKey(Area_Points_List, verbose_name='Список координат', on_delete=models.DO_NOTHING,
                                    blank=True,
                                    null=True)
    region = models.ForeignKey(Region, verbose_name='Область', on_delete=models.DO_NOTHING, blank=True,
                                    null=True)
    status_fk = models.ForeignKey(Alarm_Status, verbose_name='Тревожный статус', on_delete=models.DO_NOTHING, blank=True,
                                    null=True)

    @property
    def points(self):
        points = Area_Point.objects.filter(points_list=self.coords_list)
        data_points = Area_Point_Serializer(points, many=True)
        return data_points.data
    @property
    def status(self):
        status = self.status_fk
        return StatusSerializer(status).data
    @property
    def sensors(self):
        sensors = Sensor.objects.filter(sensor_group=self.id)
        print(sensors)
        return SensorSerializer(sensors, many=True).data

class Area_Point_Serializer(ModelSerializer):
    class Meta:
        model = Area_Point
        fields = (
            'point_coords_lat',
            'point_coords_lng',
            'array_number'
        )

class Sensor(models.Model):
    class Meta:
        verbose_name = 'Датчики'
        verbose_name_plural = 'Датчики'

    coords_list = models.ForeignKey(Area_Points_List, verbose_name='Список координат', on_delete=models.DO_NOTHING, blank=True, null=True)
    sensor_group = models.ForeignKey(Sensor_Group, verbose_name='Группа сенсеров', on_delete=models.DO_NOTHING, blank=True, null=True)
    status = models.BooleanField(verbose_name='Статус', default=False, blank=False)
    temp = models.IntegerField(verbose_name='Температура', blank=True, null=False)
    wind_direction = models.IntegerField(verbose_name='Направление ветра', blank=True, null=False, validators=[MaxValueValidator(100), MinValueValidator(0)
        ])
    wind_speed = models.IntegerField(verbose_name='Скорость ветра', blank=True, null=False)
    humidity  = models.IntegerField(verbose_name='Влажность', blank=True, null=False)
    sensor_coords_lat = models.DecimalField(verbose_name='Широта', blank=True, null=False, max_digits=10, decimal_places=6)
    sensor_coords_lng = models.DecimalField(verbose_name='Долгота', blank=True, null=False, max_digits=10, decimal_places=6)
    region = models.ForeignKey(Region, verbose_name='Область', on_delete=models.DO_NOTHING, blank=True,
                               null=True)

    @property
    def points(self):
        points = Area_Point.objects.filter(points_list=self.coords_list)
        data_points = Area_Point_Serializer(points, many=True)
        return data_points.data



class Sensor_Data_Set(models.Model):
    class Meta:
        verbose_name = 'Список показателей датчиков'
        verbose_name_plural = 'Список показателей датчиков'

    date_time = models.DateTimeField(default=datetime.now(), blank=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.DO_NOTHING, blank=False, null=False)
    temp = models.IntegerField(verbose_name='Температура', blank=True, null=False)
    wind_direction = models.IntegerField(verbose_name='Направление ветра', blank=True, null=False)
    wind_speed = models.IntegerField(verbose_name='Скорость ветра', blank=True, null=False)
    humidity = models.IntegerField(verbose_name='Влажность', blank=True, null=False)

class SensorSerializer(ModelSerializer):
    points = serializers.ReadOnlyField()

    class Meta:
        model = Sensor
        fields = (
            'status',
            'temp',
            'wind_direction',
            'wind_speed',
            'humidity',
            'sensor_coords_lat',
            'sensor_coords_lng',
            'points',
        )

class GroupSerializer(ModelSerializer):
    points = serializers.ReadOnlyField()
    status = serializers.ReadOnlyField()
    sensors = serializers.ReadOnlyField()
    class Meta:
        model = Sensor_Group
        fields = (
            'points',
            'status',
            'sensors',
        )

class StatusSerializer(ModelSerializer):
    class Meta:
        model = Alarm_Status
        fields = (
            'name',
            'status_text'
        )