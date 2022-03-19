from shapes import Shape
from shapes import Point
from shapes import PolygonShape
import math


class Triangle(PolygonShape):
    def __init__(self, center=Point(0, 0), out_color='black', in_color='white'):
        super(center, None, out_color)

    def border_coords(self):
        """
        :return: array of Points; top left and bottom right coordinates of the rectangle
        """
        # math cos and sin operate in radians
        point_A = Point(self._center.x - 10, self._center.y + 5)
        point_B = Point(self._center.x, self._center.y + 5)
        point_C = Point(self._center.x + 5, self._center.y + 5)
        self._border_coords = [point_A, point_B, point_C]
        return self._border_coords