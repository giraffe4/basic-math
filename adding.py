"""Methods for adding objects"""
from classes import Rectangle, Triangle


def add_rectangles(origin_rectangle: Rectangle, rectangle_for_adding: Rectangle) -> Rectangle:
    """Add two rectangles. Origin rectangle is extended with
    the area of rectangle_for_adding. Width and length are
    scaled accordingly. Coordinates of the left-bottom corner
    of origin_rectangle remains the same.

    Args:
        origin_rectangle (Rectangle): origin rectangle
        rectangle_for_adding (Rectangle): rectangle for adding

    Returns:
        Rectangle: new rectangle with area = origin_rectangle + rectangle_for_adding
    """
    final_rectangle = Rectangle(origin_rectangle.left_bottom, (origin_rectangle.left_bottom.x + 1, origin_rectangle.left_bottom.y + 1))
    # area = origin_rectangle.area + rectangle_for_adding.area
    return final_rectangle


def add_triangles(origin_triangle: Triangle, triangle_for_adding) -> Triangle:
    """Add two trinagles"""
    pass