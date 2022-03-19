from shapes import Shape
from shapes import Point
from shapes import PolygonShape
import math

class Diamond(PolygonShape):
    def __init__(self, center=Point(0, 0), diam=10, out_color='black', in_color='white'):
        super(center, None, out_color)
        self._diam = diam
        self._in_color = in_color

    def border_coords(self):
        """
        :return: array of Points; coordinates of the diamond's bounds
        """
        # math cos and sin operate in radians
        top_left_coord = Point(self._center._x, self._center._y + self._diam/2)
        bottom_left_coord = Point(self._center._x - self._diam / 2, self._center._y)
        top_right_coord = Point(self._center._x, self._center._y - self._diam / 2)
        bottom_right_coord = Point(self._center._x + self._diam/2)
        self._border_coords = [top_left_coord, bottom_left_coord, top_right_coord,  bottom_right_coord]
        return self._border_coords