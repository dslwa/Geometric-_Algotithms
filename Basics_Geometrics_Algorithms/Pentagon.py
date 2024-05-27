import matplotlib.pyplot as plt


class Pentagon:
    def __init__(self, v1, v2, v3, v4, v5):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4
        self.v5 = v5

    def point_in_polygon(self, point):
        num_vertices = 5
        vertices = [self.v1, self.v2, self.v3, self.v4, self.v5]
        x, y = point.x, point.y
        inside = False
        p1 = vertices[0]

        for i in range(1, num_vertices + 1):
            p2 = vertices[i % num_vertices]

            if y > min(p1.y, p2.y):
                if y <= max(p1.y, p2.y):
                    if x <= max(p1.x, p2.x):
                        x_intersection = (y - p1.y) * (p2.x - p1.x) / (p2.y - p1.y) + p1.x

                        if p1.x == p2.x or x <= x_intersection:
                            inside = not inside

            p1 = p2

        if inside:
            print("Point is inside the pentagon")
        else:
            print("Point is outside the pentagon")

    def plot(self):
        plt.plot([self.v1.x, self.v2.x, self.v3.x, self.v4.x, self.v5.x, self.v1.x],
                 [self.v1.y, self.v2.y, self.v3.y, self.v4.y, self.v5.y, self.v1.y], 'b-')
        plt.plot([self.v1.x, self.v2.x], [self.v1.y, self.v2.y], 'ro-')
        plt.plot([self.v2.x, self.v3.x], [self.v2.y, self.v3.y], 'ro-')
        plt.plot([self.v3.x, self.v4.x], [self.v3.y, self.v4.y], 'ro-')
        plt.plot([self.v4.x, self.v5.x], [self.v4.y, self.v5.y], 'ro-')
        plt.plot([self.v5.x, self.v1.x], [self.v5.y, self.v1.y], 'ro-')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Pentagon')
        plt.grid(True)
        plt.show()
