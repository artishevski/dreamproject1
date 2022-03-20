from shapes.Shape import Shape
from shapes.Point import Point
from shapes.polygon_shape.PolygonShape import PolygonShape
from shapes.polygon_shape.Line import Line
import math


class HalfLine(Line):
    def __init__(self, center=Point(0, 0), angle=0, out_color='black'):
        """
        :param center: Point; the beggining of the ray
        :param angle: int; degrees of the ray rotation level
        :param out_color: str;
        """
        super().__init__(center, angle, out_color)

    def move_center(self, new_coords: Point):
        super(HalfLine, self).move_center(new_coords)
        ray_endpoint_coord = Point(math.max * math.cos(self._angle * math.pi / 180),
                                   math.max * math.sin(self._angle * math.pi / 180))
        self._border_coords = [self._center, ray_endpoint_coord]
        return self._border_coords




