import matplotlib.pyplot as plt
import numpy as np


def plot_lab_01_ex2(line_eq, point):
    plt.title("LAB_01_ex2_ex4")
    x = point.x
    y = point.y

    a, b, c = line_eq

    x_s = np.linspace(-5, 15, 15)
    y_s = (-a * x_s - c) / b

    plt.plot(x_s, y_s, 'r-', label='Line')
    plt.plot(x, y, 'bo', label='Point')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_lab_01_ex3(line, point):
    plt.title("LAB_01_ex3")
    x = point.x
    y = point.y

    x_start = [line.start_point.x, line.end_point.x]
    y_start = [line.start_point.y, line.end_point.y]

    plt.plot(x_start, y_start, "-r", label="Line")
    plt.plot(x, y, "ro", label=f"Point: ({point.x}, {point.y})")
    plt.grid(True)
    plt.legend()
    plt.show()


def plot_lab01_ex5(line, vector):
    plt.title("LAB_01_ex5")

    x1_start = [line.start_point.x, line.end_point.x]
    y1_start = [line.start_point.y, line.end_point.y]

    a, b, c = line.translate(vector)

    x_s = np.linspace(-5, 15, 15)
    y_s = (-a * x_s - c) / b

    plt.plot(x1_start, y1_start, "-r", label="Line before translation")
    plt.plot(x_s, y_s, "-b", label="Line after translation")

    plt.grid(True)
    plt.legend()
    plt.show()


def plot_lab01_ex6(reflection_line, point_to_reflect, reflected_point):

    x_reflection = [reflection_line.start_point.x, reflection_line.end_point.x]
    y_reflection = [reflection_line.start_point.y, reflection_line.end_point.y]

    plt.plot(x_reflection, y_reflection, 'y-', label='Reflection Line')

    plt.plot(point_to_reflect.x, point_to_reflect.y, 'ro',
             label=f'Point to Reflect ({point_to_reflect.x}, {point_to_reflect.y})')

    plt.plot(reflected_point.x, reflected_point.y, 'go',
             label=f'Reflected Point ({round(reflected_point.x, 2)}, {round(reflected_point.y, 2)})')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Reflection')
    plt.grid(True)
    plt.legend()
    plt.show()


def plot_lab02_01(line1, line2):

    intersection_point = line1.cross_point(line2)
    plt.plot(intersection_point.x, intersection_point.y, 'ro',
             label=f'Cross Point ({round(intersection_point.x, 2)}, {round(intersection_point.y, 2)})')
    x_line1 = [line1.start_point.x, line1.end_point.x]
    y_line1 = [line1.start_point.y, line1.end_point.y]
    plt.plot(x_line1, y_line1, 'y-', label='Line 1')
    x_line2 = [line2.start_point.x, line2.end_point.x]
    y_line2 = [line2.start_point.y, line2.end_point.y]
    plt.plot(x_line2, y_line2, 'r-', label='Line 2')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Cross Point')
    plt.grid(True)
    plt.legend()
    plt.show()


def plot_lab02_ex2(line, point):
    plt.plot(point.x, point.y, 'ro', label=f'Point ({point.x}, {point.y})')
    x_line = [line.start_point.x, line.end_point.x]
    y_line = [line.start_point.y, line.end_point.y]
    plt.plot(x_line, y_line, 'r-', label='Line')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('LAB02_EX2')
    plt.axis('equal')
    plt.grid(True)
    plt.legend()
    plt.show()


def plot_lab02_ex3(point1, point2, point3):
    plt.plot([point1.x, point2.x], [point1.y, point2.y], 'r-', label='Line1')
    plt.plot([point2.x, point3.x], [point2.y, point3.y], 'b-', label='Line2')
    plt.plot([point3.x, point1.x], [point3.y, point1.y], 'g-', label='Line3')
    plt.plot(point1.x, point1.y, 'ro', label=f'Vertex1 ({point1.x}, {point1.y})')
    plt.plot(point2.x, point2.y, 'bo', label=f'Vertex2 ({point2.x}, {point2.y})')
    plt.plot(point3.x, point3.y, 'go', label=f'Vertex3 ({point3.x}, {point3.y})')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Triangle with Lines Passing Through Points')
    plt.grid(True)
    plt.legend()
    plt.show()


def plot_lab03_ex3(point1, point2, point3, point4):
    plt.plot([point1.x, point2.x], [point1.y, point2.y], 'r-', label='Line1')
    plt.plot([point2.x, point3.x], [point2.y, point3.y], 'b-', label='Line2')
    plt.plot([point3.x, point1.x], [point3.y, point1.y], 'g-', label='Line3')
    plt.plot(point1.x, point1.y, 'ro', label=f'Vertex1 ({point1.x}, {point1.y})')
    plt.plot(point2.x, point2.y, 'bo', label=f'Vertex2 ({point2.x}, {point2.y})')
    plt.plot(point3.x, point3.y, 'go', label=f'Vertex3 ({point3.x}, {point3.y})')
    plt.plot(point4.x, point4.y, 'ro',
             label=f'Point ({round(point4.x, 2)}, {round(point4.y, 2)})')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Triangle with Lines Passing Through Points')
    plt.grid(True)
    plt.legend()
    plt.show()


def plot_lab03_ex5(v1, v2, v3, v4, v5, point):
    plt.plot([v1.x, v2.x, v3.x, v4.x, v5.x, v1.x],
             [v1.y, v2.y, v3.y, v4.y, v5.y, v1.y], 'b-')
    plt.plot([v1.x, v2.x], [v1.y, v2.y], 'ro-')
    plt.plot([v2.x, v3.x], [v2.y, v3.y], 'ro-')
    plt.plot([v3.x, v4.x], [v3.y, v4.y], 'ro-')
    plt.plot([v4.x, v5.x], [v4.y, v5.y], 'ro-')
    plt.plot([v5.x, v1.x], [v5.y, v1.y], 'ro-')
    plt.plot(point.x, point.y, 'go', label=f'Point({point.x}, {point.y})')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Pentagon')
    plt.grid(True)
    plt.show()
