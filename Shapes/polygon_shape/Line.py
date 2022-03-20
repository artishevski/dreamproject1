from shapes import Shape
from shapes import Point
from shapes.polygon_shape import PolygonShape
import math


class Interval(PolygonShape):
    def __init__(self, center=Point(0, 0), angle=0, size=5, out_color='black'):
        """
        :param center: Point; the centre of the line
        :param angle: int; degrees of the line rotation level
        :param out_color: str;
        """
        super().__init__(center, None, out_color)
        self._angle = angle
        self._size = size

    @property
    def border_coords(self):
        """
        :return: array of Points; line begin and end points
        """
        # math cos and sin operate in radians
        left_coord = Point(self._centre._x - self._size * math.cos(self._angle*math.pi/180),
                           self._centre._y - self._size * math.sin(self._angle*math.pi/180))

        right_coord = Point(self._centre._x + self._size * math.cos(self._angle * math.pi / 180),
                            self._centre._y + self._size * math.sin(self._angle * math.pi / 180))
        self._border_coords = [left_coord, right_coord]
        return self._border_coords