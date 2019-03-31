from random import random

from django.core.management.base import BaseCommand
from backend.api.models import *

JSON_PATH = 'data'


class Command(BaseCommand):
    def handle(self, *args, **options):
        x1 = 44.505833
        x2 = 45.624839
        y1 = 56.718312
        y2 = 56.230016
        # x1 = 10
        # x2 = 190
        # y1 = 10
        # y2 = 190
        dx = (x2 - x1) / 9
        dy = (y2 - y1) / 9
        mass = []
        for i in range(10):
            line = []
            y = y1 + i * dy
            for j in range(10):
                x = x1 + j * dx
                line.append([x, y])
            # print(line)
            mass.append(line)
        areas = [[[0, 0], [0, 3], [1, 3], [4, 0]],
                 [[4, 0], [1, 3], [5, 5], [7, 4], [8, 0]],
                 [[8, 0], [7, 4], [7, 6], [9, 5], [9, 0]],
                 [[7, 6], [7, 9], [9, 9], [9, 5]],
                 [[0, 3], [0, 7], [2, 7], [5, 5], [1, 3]],
                 [[5, 5], [2, 7], [5, 9], [7, 9], [7, 4]],
                 [[0, 7], [0, 9], [5, 9], [2, 7]]]
        # for p in points:
        #     print(mass[p[0]][p[1]])
        Area_Point.objects.all()
        for a in Area_Points_List.objects.all():
            try:
                a.delete()
            except:
                print('удалить не удалось')
        print('kkkk', Area_Points_List.objects.all())
        for area_number, area in enumerate(areas):
            points_list = Area_Points_List()
            points_list.save()
            print('area_point===', points_list)
            print('area===', area)
            for array_number, point in enumerate(area):
                area_point = Area_Point(point_coords_lat=mass[point[0]][point[1]][0],
                                        point_coords_lng=mass[point[0]][point[1]][1],
                                        array_number=array_number,
                                        points_list=points_list)
                area_point.save()
