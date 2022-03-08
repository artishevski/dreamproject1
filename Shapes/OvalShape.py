from shapes.shape import Shape


class OvalShape(Shape):
    '''
    Class stores functionality for drawing oval figures with random shape
    '''
    def __init__(self, center, top_left_coord, bottom_right_coord, out_color='black', in_color='white'):
        """
        :param center: Point; coordinates of the figure centre
        :param top_left_coord: Point; top left corner coordinates
        :param bottom_right_coord: Point; bottom right corner coordinates
        :param out_color: str; color of the outer side
        :param in_color: str; color of the inner side
        """
        super().__init__(center, out_color)
        self.top_left_coord = top_left_coord
        self.bottom_right_coord = bottom_right_coord
        self.in_color = in_color
