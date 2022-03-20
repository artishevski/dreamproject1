from shapes import Shape
from shapes.Point import Point
from shapes.polygon_shape.PolygonShape import PolygonShape
import math

class Square(PolygonShape):
    def __init__(self, center=Point(0, 0), width=50, out_color='red', in_color='blue'):
        super().__init__(center, None, out_color, in_color)
        self._width = width
        self._in_color = in_color

    def move_center(self, new_coords: Point):
        super(Square, self).move_center(new_coords)
        top_left_coord = Point(self._center._x - self._width/2, self._center._y - self._width/2)
        bottom_left_coord = Point(self._center._x - self._width / 2, self._center._y + self._width / 2)
        top_right_coord = Point(self._center._x + self._width / 2, self._center._y + self._width / 2)
        bottom_right_coord = Point(self._center._x + self._width/2, self._center._y - self._width/2)
        self._border_coords = [top_left_coord, bottom_left_coord, top_right_coord,  bottom_right_coord]