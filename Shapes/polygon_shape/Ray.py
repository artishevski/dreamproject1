from shapes import Shape
from shapes import Point
from shapes import PolygonShape
import math


class Ray(PolygonShape):
    def __init__(self, center=Point(0, 0), angle=0, out_color='black'):
        """
        :param center: Point; the beggining of the ray
        :param angle: int; degrees of the ray rotation level
        :param out_color: str;
        """
        super().__init__(center, None, out_color)
        self._angle = angle

    @property
    def border_coords(self):
        """
        :return: array of Points; ray begin and end points (infinity)
        """
        # math cos and sin operate in radians
        ray_endpoint_coord = Point(math.max * math.cos(self._angle*math.pi/180),
                                   math.max * math.sin(self._angle*math.pi/180))
        self._border_coords = [self._center, ray_endpoint_coord]
        return self._border_coords



