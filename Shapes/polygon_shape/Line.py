from shapes.Shape import Shape
from shapes.Point import Point
from shapes.polygon_shape.PolygonShape import PolygonShape
import math


class Line(PolygonShape):
    def __init__(self, center=Point(0, 0), angle=0, out_color='black'):
        """
        :param center: Point; the centre of the line
        :param angle: int; degrees of the line rotation level
        :param out_color: str;
        """
        super().__init__(center, None, out_color)
        self._angle = angle

    def move_center(self, new_coords: Point):
        super(Line, self).move_center(new_coords)
        left_coord = Point(self._centre._x - math.max * math.cos(self._angle * math.pi / 180),
                           self._centre._y - math.max * math.sin(self._angle * math.pi / 180))
        right_coord = Point(self._centre._x + math.max * math.cos(self._angle * math.pi / 180),
                            self._centre._y + math.max * math.sin(self._angle * math.pi / 180))
        self._border_coords = [left_coord, right_coord]
        return self._border_coords