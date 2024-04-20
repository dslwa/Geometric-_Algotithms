from Punkt import Point
import math


class Line:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def equation(self):
        x1 = self.start_point.x
        y1 = self.start_point.y
        x2 = self.end_point.x
        y2 = self.end_point.y
        if x1 == x2:
            a = 0
            b = -1
            c = x1
        else:
            a = (y1 - y2) / (x1 - x2)
            b = -1
            c = y1 - (x1 * ((y1 - y2) / (x1 - x2)))
        return a, b, c

    def belonging_to_line(self, point):
        a, b, c = self.equation()
        result = point.x * a + point.y * b + c
        return result

    def is_on_line(self, point):
        belonging = self.belonging_to_line(point)
        if belonging == 0:
            print("Point belongs to line")
        elif belonging > 0:
            print("Point is on the right")
        else:
            print("Point is on the left")

    def conditions(self):
        x1 = self.start_point.x
        y1 = self.start_point.y
        x2 = self.end_point.x
        y2 = self.end_point.y
        cond1 = min(x1, x2)
        cond2 = max(x1, x2)
        cond3 = min(y1, y2)
        cond4 = max(y1, y2)
        return cond1, cond2, cond3, cond4

    def is_point_on_segment(self, point):
        cond1, cond2, cond3, cond4 = self.conditions()
        belonging = self.belonging_to_line(point)
        if belonging == 0 and cond1 < point.x < cond2 and cond3 < point.y < cond4:
            return True
        else:
            return False

    def translate(self, vector):
        self.start_point.x += vector[0]
        self.start_point.y += vector[1]
        self.end_point.x += vector[0]
        self.end_point.y += vector[1]
        return self.equation()

    def reflect_point(self, point):
        a, _, _ = self.equation()
        c = point.y + (1 / a) * point.x
        x_intersect = (c - self.start_point.y + a * self.start_point.x) / (a + 1 / a)
        y_intersect = a * x_intersect + self.start_point.y - a * self.start_point.x
        x_reflected = 2 * x_intersect - point.x
        y_reflected = 2 * y_intersect - point.y
        return Point(x_reflected, y_reflected)

    def cross_point(self, line):
        a1, b1, c1 = self.equation()
        a2, b2, c2 = line.equation()

        determinant = a1 * b2 - a2 * b1
        if determinant == 0:
            return None

        x = (b1 * c2 - b2 * c1) / determinant
        y = (a2 * c1 - a1 * c2) / determinant
        return Point(x, y)

    def cross_point_bool(self, line):
        a1, b1, c1 = self.equation()
        a2, b2, c2 = line.equation()
        determinant = a1 * b2 - a2 * b1
        if determinant == 0:
            return False
        else:
            return True

    def distance_to_point(self, point):
        a, b, c = self.equation()
        distance = abs(a * point.x + b * point.y + c) / ((a ** 2 + b ** 2) ** 0.5)
        return distance

    def angle_between_lines(self, other_line):

        vector1 = (self.end_point.x - self.start_point.x, self.end_point.y - self.start_point.y)
        vector2 = (other_line.end_point.x - other_line.start_point.x, other_line.end_point.y - other_line.start_point.y)

        dot_product = vector1[0] * vector2[0] + vector1[1] * vector2[1]

        magnitude1 = math.sqrt(vector1[0] ** 2 + vector1[1] ** 2)
        magnitude2 = math.sqrt(vector2[0] ** 2 + vector2[1] ** 2)

        angle_rad = math.acos(dot_product / (magnitude1 * magnitude2))

        angle_deg = math.degrees(angle_rad)

        return angle_deg
