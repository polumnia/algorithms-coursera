from functools import total_ordering
from collections import Counter
import math

@total_ordering
class Point():
    """Data type for points in the plane."""
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __lt__(self, other):
        if self.y < other.y:
            return True
        elif self.y == other.y:
            return self.x < other.x
        return False

    def slope_to(self, other):
        if self.x == other.x:
            if self.y == other.y:
                return (- math.inf)
            return math.inf
        return (other.y - self.y) / (other.x - self.x)

class LineSegment:
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __str__(self):
        return f"{self.p} -> {self.q}"


class FastCollinearPoints():
    def __init__(self, points):
        self.points = sorted(points)

    def number_of_segments(self):
        number_of_segments = 0
        for id, point in enumerate(self.points):
            segment = find_max_line_segment(point, self.points[id:])
            if segment:
                number_of_segments += 1
        return number_of_segments

    def segments(self):
        for id, point in enumerate(self.points):
            segment = find_max_line_segment(point, self.points[id:])
            if segment:
                yield segment

def find_max_line_segment(origin_point, other_points):
    point_slopes = dict()
    for point in other_points:
        slope = origin_point.slope_to(point)
        if slope in point_slopes:
            point_slopes[slope].append(point)
        else:
            point_slopes[slope] = [point]
    slope, segment = max(point_slopes.items(), key=lambda x: len(x[1]))
    if len(segment) >= 3:
        return LineSegment(origin_point, max(segment))
    return None

if __name__ == '__main__':
    coordinates = [
        [19000, 10000],
        [18000, 10000],
        [32000, 10000],
        [21000, 10000],
        [1234,  5678],
        [14000, 10000]
    ]
    points = [Point(x,y) for x, y in coordinates]

    collinear = FastCollinearPoints(points)
    print(collinear.number_of_segments())

    for segment in collinear.segments():
        print(segment)
