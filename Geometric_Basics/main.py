from GeomettiaObliczeniowaLab01_02.Pentagon import Pentagon
from Visualisation import *
from Test import *
from Triangle import Triangle

print("LAB_01_01")
point1 = Point(0, 1)
point2 = Point(4, 4)
line1 = Line(point1, point2)
a, b, c = line1.equation()
print("Line equation: y =", a, "x +", c)

print("LAB_01_02")

point3 = Point(1, 1.75)
line1.is_on_line(point3)
# plot_lab_01_ex2(line1.equation(), point3)

print("LAB_01_03")

if line1.is_point_on_segment(point3):
    print("Point on segment")
else:
    print("Point in not on segment")

# plot_lab_01_ex3(line1, point3)

print("LAB_01_04")
point4 = Point(10, 10)
line1.is_on_line(point4)
# plot_lab_01_ex2(line1.equation(), point4)

print("LAB_01_05")
v = [1, 4]
line1.translate(v)
# plot_lab01_ex5(line1, v)

print("LAB_01_06")
line2 = Line(point3, point4)
line2.reflect_point(point1)
print("Point before reflection(", point1.x, ",", point1.y, ")")
print("Point after reflection(", round(line2.reflect_point(point1).x, 2), ",", round(line2.reflect_point(point1).y, 2),
      ")")

# plot_lab01_ex6(line2, point1, line2.reflect_point(point1))

print("LAB_02_01")
point5 = Point(1, 1)
point6 = Point(19, 19)

point7 = Point(15, 23)
point8 = Point(2.5, 0)

line3 = Line(point5, point6)
line4 = Line(point7, point8)

res = line3.cross_point(line4)
print("Cross Point", round(res.x, 2), "", round(res.y, 2))
# plot_lab02_01(line3, line4)

print("LAB_02_02")

print("Distance:", round(line3.distance_to_point(point1), 2))

# plot_lab02_ex2(line3, point1)

print("LAB_02_03")

point11 = Point(1, 1)
point12 = Point(4, 4)
point13 = Point(8, 1)

line_eq1 = (1, -1, 0)
line_eq2 = (0.5, -1, 0)
line_eq3 = (-1, -1, 7)

triangle = Triangle(point11, point12, point13)
triangle1 = Triangle.create_triangle(line_eq1, line_eq2, line_eq3)

# plot_lab02_ex3(triangle.v1, triangle.v2, triangle.v3)
# plot_lab02_ex3(triangle.v1, triangle1.v2, triangle1.v3)

print("LAB_03_01")
print("Area of triangle is  ", triangle.calculate_triangle_area())
print("Area of triangle is  ", round(triangle1.calculate_triangle_area(), 2))


print("LAB_03_02")
line11 = Line(point11, point12)
line12 = Line(point12, point13)
print("Angle of lines ", line11.angle_between_lines(line12))
# plot_lab02_01(line11, line12)

print("LAB_03_03")
triangle.is_point_inside_triangle(Point(3, 3))
triangle.is_point_inside_triangle(Point(9, 3))
triangle.location_of_point_2nd_method(Point(3, 3))
triangle.location_of_point_2nd_method(Point(9, 3))
plot_lab03_ex3(triangle.v1, triangle.v2, triangle.v3, Point(4, 3))
plot_lab03_ex3(triangle.v1, triangle.v2, triangle.v3, Point(9, 3))
print("LAB_03_04")

v1, v2, v3 = Point(1, 1), Point(4, 1), Point(6, 5)
v4, v5 = Point(4, 5), Point(2, 7)
p1 = Pentagon(v1, v2, v3, v4, v5)
p1.plot()

print("LAB_03_05")
print(p1.point_in_polygon(Point(3, 4)))
print(p1.point_in_polygon(Point(10, 1)))
plot_lab03_ex5(v1, v2, v3, v4, v5, Point(10, 1))
plot_lab03_ex5(v1, v2, v3, v4, v5, Point(3, 4))
