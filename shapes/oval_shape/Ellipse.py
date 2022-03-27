from shapes.oval_shape.OvalShape import *
from shapes.Shape import Shape
from shapes.Point import Point

class Ellipse(OvalShape):
    """
    Class provides functionality for creating circles with the fied size
    """

    def __init__(self, center = Point(0, 0), width=60, height=30, out_color='red', in_color='blue'):
        """
        :param center: Point; coordinates of the figure centre
        :param radius: int; radius of the circle
        :param out_color: str; color of the outer side
        :param in_color: str; color of the inner side
        """
        super().__init__(center, None, None, out_color, in_color)
        self._width = width
        self._heigth = height

    def move_center(self, new_coords: Point):
        super(Ellipse, self).move_center(new_coords)
        self._top_left_coord = Point(self._center._x-self._width, self._center._y - self._heigth)
        self._bottom_right_coord = Point(self._center._x + self._width, self._center._y + self._heigth)