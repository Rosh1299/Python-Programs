# Creating a class


class Point():
    # class attributes
    default_color = "red"
    # Creating constructor

    def __init__(self, x, y):
        # instance attributes
        self.x = x
        self.y = y

    # instance Method
    def draw(self):
        print(f"Point({self.x},{self.y})")


point = Point(1, 2)
point.draw()
# print(type(point))
# print(isinstance(point, int))
# print(point.y)
print(point.default_color)
print(Point.default_color)
Point.default_color = "Yellow"
print(Point.default_color)


print(point.__dict__)
