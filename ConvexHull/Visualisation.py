import matplotlib.pyplot as plt


def visualize(points, convex_hull):

    x_coords = [point.x for point in points]
    y_coords = [point.y for point in points]

    hull_x_coords = [point.x for point in convex_hull]
    hull_y_coords = [point.y for point in convex_hull]

    plt.scatter(x_coords, y_coords, color='red', label='Points')
    plt.plot(hull_x_coords + [hull_x_coords[0]], hull_y_coords + [hull_y_coords[0]], color='blue', linestyle='-', linewidth=2, label='Convex Hull')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Otoczka')
    plt.legend()
    plt.grid(True)
    plt.show()
