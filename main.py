from adding import add_rectangles
from classes import Rectangle, Point

if __name__ == "__main__":

    rectangle_1 = Rectangle(Point(0, 0), Point(1, 1))

    rectangle = add_rectangles(rectangle_1, rectangle_1)