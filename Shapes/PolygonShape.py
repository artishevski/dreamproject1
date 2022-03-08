from shapes.shape import Shape


class PolygonShape(Shape):
    """
    Basic class for polygon creation
    """
    def __init__(self, center=Point(0, 0), border_coords=[], out_color='black'):
        """
        :param center: Point; coordinates of the figure centre
        :param border_coords: list of Points; coordinates of the polygon's sides
        :param out_color: str; color of the outer side
        """
        super().__init__(center, out_color)
        self._border_coords = border_coords
