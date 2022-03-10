from shapes.oval_shape.OvalShape import *
from shapes.Shape import Shape
from shapes.Point import Point

class Circle(OvalShape):
    """
    Class provides functionality for creating circles with the fied size
    """

    def __init__(self, center, radius=5, out_color='black', in_color='white'):
        """
        :param center: Point; coordinates of the figure centre
        :param radius: int; radius of the circle
        :param out_color: str; color of the outer side
        :param in_color: str; color of the inner side
        """
        super().__init__(center, None, None, out_color, in_color)
        self.radius = radius


    @property
    def top_left_coord(self):
        """
        :return: Point; top_left_coord of the circle
        """
        self._top_left_coord = Point(self._center._x-self.radius, self._center._y + self.radius)
        return self._top_left_coord

    @property
    def bottom_right_coord(self):
        self._bottom_right_coord = Point(self._center._x + self.radius, self._center._y - self.radius)
        return self._bottom_right_coord