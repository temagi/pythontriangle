from triangle.triangle_type import TriangleType


def triangle(a: int, b: int, c: int) -> TriangleType:
    # TODO: should we check triangle for possibility?
    if a == b == c:
        return TriangleType.EQUILATERAL
    elif a == b or a == c or b == c:
        return TriangleType.ISOSCELES
    else:
        return TriangleType.SCALENE
