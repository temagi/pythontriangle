from triangle.calculate_triangle import triangle
from triangle.triangle_type import TriangleType


def test_equal():
    assert triangle(3, 3, 3) == TriangleType.EQUILATERAL


def test_isosceles():
    assert triangle(3, 3, 2) == TriangleType.ISOSCELES


def test_():
    assert triangle(4, 3, 2) == TriangleType.SCALENE
