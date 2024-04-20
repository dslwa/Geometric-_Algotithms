from jarvis_algorithm import *


def polar_angle(p0, p1):
    if p0.y == p1.y:
        return -math.pi
    dy = p0.y - p1.y
    dx = p0.x - p1.x
    return math.atan2(dy, dx)


def graham(points):
    p0 = min(points, key=lambda p: (p.y, p.x))
    points.sort(key=lambda p: (polar_angle(p0, p), distance(p0, p)))
    hull = []
    for i in range(len(points)):
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], points[i]) != 1:
            hull.pop()
        hull.append(points[i])
    return hull
