from triangle.triangle_type import TriangleType


def triangle(a: int, b: int, c: int) -> TriangleType:
    if a + b <= c or a + c <= b or b + c <= a:
        return TriangleType.IMPOSSIBLE
    if a == 0 or b == 0 or c == 0:
        return TriangleType.IMPOSSIBLE
    elif a == b == c:
        return TriangleType.EQUILATERAL
    elif a == b or a == c or b == c:
        return TriangleType.ISOSCELES
    else:
        return TriangleType.SCALENE
