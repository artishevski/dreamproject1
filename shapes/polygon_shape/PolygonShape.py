from shapes.Shape import Shape
from shapes.Point import Point


class PolygonShape(Shape):
    """
    Basic class for polygon creation
    """
    def __init__(self, center=Point(0, 0), border_coords=[], out_color='red', in_color ='blue'):
        """
        :param center: Point; coordinates of the figure centre
        :param border_coords: list of Points; coordinates of the polygon's sides
        :param out_color: str; color of the outer side
        """
        super().__init__(center, out_color, in_color)
        self._border_coords = border_coords

    #def set_border_coords(self):

