import math
from dataclasses import dataclass
from typing import Optional

class Point2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to(self, that):
        return math.sqrt(self.distance_squared_to(that))
    
    def distance_squared_to(self, that):
        return (self.x - that.x) ^2 + (self.y - that.y) ^ 2
    
    def __eq__(self, that):
        return self.x == that.x and self.y == that.y
    
    def __str__(self):
        return f"({self.x}, {self.y})"


class RectHV:
    def __init__(self, xmin, ymin, xmax, ymax):
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax
        self._center = Point2D(
            (self.xmax - self.xmin) / 2,
            (self.ymax - self.ymin) / 2)
    
    def contains(self, point):
        return (self.xmin <= point.x <= self.xmax) and (self.ymin <= point.y <= self.ymax)
    
    def intersects(self, that):
        if self.xmax < that.xmin or that.xmax < self.xmin:
            return False
        
        if self.ymax < that.ymin or that.ymax < self.ymin:
            return False
        
        return True
    
    def distance_to(self, point):
        return math.sqrt(self.distance_squared_to(point))

    def distance_squared_to(self, point):
        dx = max(abs(point.x - self._center.x) - self._center.x, 0)
        dy = max(abs(point.y - self._center.y) - self._center.y, 0)
        return dx * dx + dy * dy

    def __eq__(self, that):
        return (
            self.xmin == that.xmin and
            self.xmax == that.xmax and
            self.ymin == that.ymin and
            self.ymax == that.ymax
        )

    
    def __str__(self):
        pass


class PointSet:
    @dataclass
    class KDNode:
        point: 'Point2D'
        left: Optional['KDNode'] = None
        right: Optional['KDNode'] = None
        level: int = 1
        
    def __init__(self):
        self.size = 0
        self.kd_root = None
    
    def _insert(self, subtree, point, level=1):
        if subtree is None:
            self.size += 1
            return self.KDNode(point, level=level)
        
        if subtree.level % 2 == 1:
            if point.x <= subtree.point.x:
                subtree.left = self._insert(subtree.left, point, level + 1)
            else:
                subtree.right = self._insert(subtree.right, point, level + 1)
        else:
            if point.y <= subtree.point.y:
                subtree.left = self._insert(subtree.left, point, level + 1)
            else:
                subtree.right = self._insert(subtree.right, point, level + 1)
        return subtree

    def insert(self, point: Point2D):
        if self.contains(point):
            return

        self.kd_root = self._insert(self.kd_root, point)
    
    def contains(self, point):
        current_node = self.kd_root
        while True:
            if current_node is None:
                return False
            
            if current_node.point == point:
                return True

            if current_node.level % 2 == 1:
                if point.x <= current_node.point.x:
                    current_node = current_node.left
                else:
                    current_node = current_node.right
            else:
                if point.y <= current_node.point.y:
                    current_node = current_node.left
                else:
                    current_node = current_node.right
    
    def _range(self, subtree, rect: RectHV):
        if subtree is None:
            return
        
        current_point = subtree.point

        if rect.contains(current_point):
            yield current_point
        
        if subtree.level % 2 == 1:
            if rect.xmax < current_point.x:
                yield from self._range(subtree.left, rect)
            elif current_point.x < rect.xmin:
                yield from self._range(subtree.right, rect)
            else:
                yield from self._range(subtree.left, rect)
                yield from self._range(subtree.right, rect)
        else:
            if rect.ymax < current_point.y:
                yield from self._range(subtree.left, rect)
            elif current_point.y < rect.ymin:
                yield from self._range(subtree.right, rect)
            else:
                yield from self._range(subtree.left, rect)
                yield from self._range(subtree.right, rect)

    def range(self, rect: RectHV):
        yield from self._range(self.kd_root, rect)
    
    def _nearest(self, subtree, nearest_point, query_point):
        if subtree is None:
            return nearest_point

        if query_point.distance_to(subtree.point) < query_point.distance_to(nearest_point):
            nearest_point = subtree.point


    def nearest(self, point):
        closest_node = self.kd_root



if __name__ == '__main__':
    points = [
        (0.7, 0.2),
        (0.5, 0.4),
        (0.2, 0.3),
        (0.4, 0.7),
        (0.9, 0.6)
    ]
    p_set = PointSet()
    for x, y in points:
        p_set.insert(Point2D(x, y))
    print(p_set.size)

    rect = RectHV(0.25, 0.25, 0.75, 0.75)
    print(rect.contains(Point2D(4, 4)))
    print(rect.distance_squared_to(Point2D(0.4, 0.4)))
    for p in p_set.range(RectHV(0.1, 0.1, 0.7, 0.5)):
        print(p)
