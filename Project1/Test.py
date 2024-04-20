from Punkt import Point
from Line import Line
import unittest


class TestLineFunctions(unittest.TestCase):

    def test_equation(self):
        point1 = Point(1, 1)
        point2 = Point(3, 3)
        line = Line(point1, point2)
        a, b, c = line.equation()
        self.assertEqual((a, b, c), (1.0, -1, 0))

    def test_belonging_to_line(self):
        point1 = Point(1, 1)
        point2 = Point(3, 3)
        line = Line(point1, point2)
        point3 = Point(2, 2)
        result = line.belonging_to_line(point3)
        self.assertEqual(result, 0)

    def test_is_on_line(self):
        point1 = Point(1, 1)
        point2 = Point(3, 3)
        line = Line(point1, point2)
        point3 = Point(2, 2)
        self.assertEqual(line.is_on_line(point3), 0)

    def test_conditions(self):
        point1 = Point(1, 1)
        point2 = Point(3, 3)
        line = Line(point1, point2)
        cond1, cond2, cond3, cond4 = line.conditions()
        self.assertEqual((cond1, cond2, cond3, cond4), (1, 3, 1, 3))

    def test_is_point_on_segment(self):
        point1 = Point(1, 1)
        point2 = Point(3, 3)
        line = Line(point1, point2)
        point3 = Point(2, 2)
        self.assertTrue(line.is_point_on_segment(point3))

    def test_translate(self):
        point1 = Point(1, 1)
        point2 = Point(3, 3)
        line = Line(point1, point2)
        original_equation = line.equation()
        translated_equation = line.translate([1, 2])
        self.assertNotEqual(original_equation, translated_equation)

    def test_reflection(self):
        point1 = Point(0, 1)
        point2 = Point(4, 5)
        point_to_reflect = Point(3, 0)
        line1 = Line(point1, point2)
        reflected_point = line1.reflect_point(point_to_reflect)
        self.assertEqual((reflected_point.x, reflected_point.y), (-1, 4))
