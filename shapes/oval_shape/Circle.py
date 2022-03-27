from shapes.oval_shape.OvalShape import *
from shapes.Point import Point

class Circle(OvalShape):
    """
    Class provides functionality for creating circles with the fied size
    """

    def __init__(self, radius=30, center=Point(0, 0), out_color='red', in_color='blue'):
        """
        :param center: Point; coordinates of the figure centre
        :param radius: int; radius of the circle
        :param out_color: str; color of the outer side
        :param in_color: str; color of the inner side
        """
        super().__init__(None, None, center, out_color, in_color)
        self.radius = radius

    def move_center(self, new_coords: Point):
        super(Circle, self).move_center(new_coords)
        self._top_left_coord = Point(self._center._x-self.radius, self._center._y - self.radius)
        self._bottom_right_coord = Point(self._center._x + self.radius, self._center._y + self.radius)