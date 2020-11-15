from triangle.calculate_triangle import triangle
from triangle.triangle_type import TriangleType
import pytest


def test_equal():
    assert triangle(3, 3, 3) == TriangleType.EQUILATERAL


def test_isosceles():
    assert triangle(3, 3, 2) == TriangleType.ISOSCELES


def test_scalene():
    assert triangle(4, 3, 2) == TriangleType.SCALENE


@pytest.mark.parametrize("a, b, c", [(2, 3, 6), (3, 2, 5), (6, 3, 2), (5, 2, 3), (2, 6, 3), (3, 5, 2), (0, 1, 1), (1, 0, 1)])
def test_possibility(a, b, c):
    assert triangle(a, b, c) == TriangleType.IMPOSSIBLE
