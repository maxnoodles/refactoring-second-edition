# -*- coding:utf-8 -*-
#
# Author: noodles
# Date: 2020-04-19
import math

points = []

def track_summary_source(points):
    def distance(p1, p2):
        EARTH_RADIUS = 3959  # in miles
        dLat = radians(p2.lat) - radians(p1.lat)
        dLon = radians(p2.lon) - radians(p1.lon)
        a = math.pow(math.sin(dLat / 2), 2) + \
            math.cos(radians(p2.lat)) * \
            math.cos(radians(p1.lat)) * \
            math.pow(math.sin(dLon / 2), 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return EARTH_RADIUS * c

    def radians(degrees):
        return degrees * math.pi / 180

    def calculate_time():
        return 0

    def calculate_distance():
        result = 0
        for i in range(1, len(points)):
            result += distance(points[i - 1], points[i])
        return result

    totalTime = calculate_time()
    totalDistance = calculate_distance()
    pace = totalTime / 60 / totalDistance
    return {
        'time': totalTime,
        'distance': totalDistance,
        'pace': pace
    }


def track_summary(points):
    def calculate_time():
        return 0

    totalTime = calculate_time()
    pace = totalTime / 60 / total_distance(points)
    return {
        'time': totalTime,
        'distance': total_distance(points),
        'pace': pace
    }


def total_distance(points):
    result = 0
    for i in range(1, len(points)):
        result += distance(points[i - 1], points[i])
    return result


def radians(degrees):
    return degrees * math.pi / 180


def distance(p1, p2):
    EARTH_RADIUS = 3959  # in miles
    dLat = radians(p2.lat) - radians(p1.lat)
    dLon = radians(p2.lon) - radians(p1.lon)
    a = math.pow(math.sin(dLat / 2), 2) + \
        math.cos(radians(p2.lat)) * \
        math.cos(radians(p1.lat)) * \
        math.pow(math.sin(dLon / 2), 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return EARTH_RADIUS * c

