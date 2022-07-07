from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: float
    y: float

@dataclass(frozen=True)
class Rectangle:
    left_bottom: Point
    right_top: Point

    def area(self) -> float:
        """Return area of the rectangle"""
        width = (self.left_bottom.x + self.right_top.x) / 2
        length = (self.left_bottom.y + self.right_top.y) / 2
        return width * length

@dataclass(frozen=True)
class Triangle:
    first_point: Point
    second_point: Point
    third_point: Point

@dataclass(frozen=True)
class Circle:
    center: Point
    radius: float