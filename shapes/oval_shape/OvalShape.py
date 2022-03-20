from shapes.Shape import Shape
from shapes.Point import Point

class OvalShape(Shape):
    '''
    Class stores functionality for drawing oval figures with random shape
    '''
    def __init__(self, top_left_coord, bottom_right_coord, center=Point(0, 0), out_color='blue', in_color='red'):
        """
        :param center: Point; coordinates of the figure centre
        :param top_left_coord: Point; top left corner coordinates
        :param bottom_right_coord: Point; bottom right corner coordinates
        :param out_color: str; color of the outer side
        :param in_color: str; color of the inner side
        """
        super().__init__(center, out_color, in_color)
        self._top_left_coord = top_left_coord
        self._bottom_right_coord = bottom_right_coord