from Visualisation import *
from Point import Point
import math


def read_file(name):
    points = []
    with open(name, 'r') as file:
        for line in file:
            try:
                x, y = map(int, line.split())
                point = Point(x, y)
                points.append(point)
            except ValueError:
                print(f"Ignoring invalid line: {line.strip()}")

    return points


def distance(point1, point2):
    x1, x2, y1, y2 = point1.x, point2.x, point1.y, point2.y
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


def orientation(p1, p2, p3):
    val = (p2.y - p1.y) * (p3.x - p2.x) - (p2.x - p1.x) * (p3.y - p2.y)
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return -1


def jarvis_march(points):

    n = len(points)
    if n < 3:
        return "Convex hull not possible"

    start = min(points, key=lambda p: (p.x, p.y))
    hull = []
    on_hull = start

    while True:
        hull.append(on_hull)
        next_point = points[0]
        for point in points:
            o = orientation(on_hull, next_point, point)
            if (next_point == on_hull or o == 1
            or o == 0 and distance(on_hull, point) > distance(on_hull, next_point)):
                next_point = point

        on_hull = next_point
        if next_point == start:
            break

    return hull


points = read_file("ksztalt_2.txt")
convex_hull = jarvis_march(points)

visualize(points, convex_hull)

points2 = read_file("ksztalt_3.txt")
convex_hull2 = jarvis_march(points2)

visualize(points2, convex_hull2)

points3 = read_file("ksztalt_4.txt")
convex_hull3 = jarvis_march(points3)

visualize(points3, convex_hull3)
