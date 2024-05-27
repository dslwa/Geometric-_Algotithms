from Punkt import Point
from Line import Line


class Triangle:

    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

    @staticmethod
    def create_triangle(line_eq1, line_eq2, line_eq3):
        a1, b1, c1 = line_eq1
        a2, b2, c2 = line_eq2
        a3, b3, c3 = line_eq3

        x1 = (b1 * c2 - b2 * c1) / (a1 * b2 - a2 * b1)
        y1 = (a1 * c2 - a2 * c1) / (a2 * b1 - a1 * b2)

        x2 = (b2 * c3 - b3 * c2) / (a2 * b3 - a3 * b2)
        y2 = (a2 * c3 - a3 * c2) / (a3 * b2 - a2 * b3)

        x3 = (b3 * c1 - b1 * c3) / (a3 * b1 - a1 * b3)
        y3 = (a3 * c1 - a1 * c3) / (a1 * b3 - a3 * b1)

        point1 = Point(x1, y1)
        point2 = Point(x2, y2)
        point3 = Point(x3, y3)

        return Triangle(point1, point2, point3)

    def calculate_triangle_area(self):
        area = abs(0.5 * (self.v2.x * self.v3.y - self.v2.x * self.v1.y - self.v1.x * self.v3.y -
                          self.v3.x * self.v2.y + self.v3.x * self.v1.y + self.v1.x * self.v2.y))
        return area

    def is_point_inside_triangle(self, point):
        tolerance = 1e-5
        area = self.calculate_triangle_area()
        t1 = Triangle(point, self.v1, self.v2)
        t2 = Triangle(point, self.v2, self.v3)
        t3 = Triangle(point, self.v1, self.v3)
        t1_area = t1.calculate_triangle_area()
        t2_area = t2.calculate_triangle_area()
        t3_area = t3.calculate_triangle_area()
        print(area, t1_area, t2_area, t3_area, t1_area + t2_area + t3_area)
        if abs(area - (t1_area + t2_area + t3_area)) < tolerance:
            print("Point is inside the triangle")
        else:
            print("Point is outside the triangle")

    def location_of_point_2nd_method(self, point):
        tolerance = 1e-4
        line1 = Line(point, self.v1)
        line2 = Line(point, self.v2)
        line3 = Line(point, self.v3)

        angle1 = line1.angle_between_lines(line2)
        angle2 = line1.angle_between_lines(line3)
        angle3 = line2.angle_between_lines(line3)

        angle = angle1 + angle2 + angle3

        if abs(360 - angle) < tolerance:
            print("Point is inside the triangle")
        else:
            print("Point is outside of the triangle")
