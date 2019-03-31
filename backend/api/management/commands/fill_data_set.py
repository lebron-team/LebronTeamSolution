import random
import time

from django.core.management.base import BaseCommand
from backend.api.models import *

JSON_PATH = 'data'


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('qqq')
        sensors = Sensor.objects.all()
        Sensor_Data_Set.objects.all().delete()
        print(sensors)
        for s in sensors:
            s.temp = random.randint(10, 15)
            s.humidity = random.randint(30, 50)
            s.save()
        i = 0
        k = 0
        iteration = 0
        while True:
            iteration += 1
            if k == 100:
                break
            amount = 2
            time.sleep(amount)
            numberr = 0
            sen_number = random.randint(0, (len(sensors) - 1))
            for s in sensors:
                number =+ 1
                wind_direction = random.randint(80, 90)
                wind_speed = random.randint(20, 25)
                print(number, sen_number)
                if iteration % 5 == 0 and numberr == sen_number:
                    print('Повезло')
                    if s.temp <= 100:
                        new_temp = s.temp + 5
                    if s.humidity >= 10:
                        new_humidity = s.humidity - 2
                    sensor_data_set = Sensor_Data_Set(sensor=s, temp=new_temp,
                                                    wind_direction=wind_direction, wind_speed=wind_speed, humidity=new_humidity)
                    sensor_data_set.save()
                    s.temp = new_temp
                    s.humidity = new_humidity
                    s.wind_direction = wind_direction
                    s.wind_speed = wind_speed
                    s.save
                    continue
                sensor_data_set = Sensor_Data_Set(sensor=s, temp=s.temp,
                                                  wind_direction=wind_direction, wind_speed=wind_speed,
                                                  humidity=s.humidity)
                sensor_data_set.save()
                s.wind_direction = wind_direction
                s.wind_speed = wind_speed
                s.save()
            iteration =+ 1
            k =+ 1