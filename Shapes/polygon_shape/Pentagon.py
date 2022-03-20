from shapes import Shape
from shapes.Point import Point
from shapes.polygon_shape.PolygonShape import PolygonShape
import math


class Pentagon(PolygonShape):
    def __init__(self, center=Point(0, 0), out_color='red', in_color='blue'):
        super().__init__(center, None, out_color, in_color)

    def move_center(self, new_coords: Point):
        super(Pentagon, self).move_center(new_coords)
        point_A = Point(self._center._x - 30, self._center._y + 30)
        point_B = Point(self._center._x + 30, self._center._y + 30)
        point_C = Point(self._center._x -40, self._center._y - 20)
        point_D = Point(self._center._x, self._center._y -50)
        point_E = Point(self._center._ + 40, self._center._y - 20)
        self._border_coords = [point_A, point_B, point_C, point_D, point_E]