from shapes.Shape import Shape
from shapes.Point import Point
from shapes.polygon_shape.PolygonShape import PolygonShape
from shapes.polygon_shape.Line import Line
from shapes.polygon_shape.HalfLine import HalfLine
import math


class Interval(HalfLine):
    def __init__(self, center=Point(0, 0), angle=45, size=50, out_color='black'):
        """
        :param center: Point; the centre of the Line
        :param angle: int; degrees of the line rotation level
        :param out_color: str;
        """
        super().__init__(center, angle, out_color)
        self._size = size


    def move_center(self, new_coords: Point):
        super(Interval, self).move_center(new_coords)
        left_coord = Point(self._center._x - self._size / 2 * math.cos(self._angle * math.pi / 180),
                           self._center._y - self._size / 2 * math.sin(self._angle * math.pi / 180))

        right_coord = Point(self._center._x + self._size / 2 * math.cos(self._angle * math.pi / 180),
                            self._center._y + self._size / 2 * math.sin(self._angle * math.pi / 180))
        self._border_coords = [left_coord, right_coord]
