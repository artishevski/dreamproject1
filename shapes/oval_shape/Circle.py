from shapes.oval_shape.OvalShape import OvalShape
from shapes.Point import *
from shapes.Shape import *

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
        self.top_left_coord = Point(self.center.x-self.radius, self.center.y + self.radius)
        return self.top_left_coord

    @property
    def bottom_left_coord(self):
        self.bottom_right_coord = Point(self.center.x + self.radius, self.center.y - self.radius)
        return self.bottom_right_coord

