from shapes.Point import Point


class Shape:
    def __init__(self, center=Point(0, 0), out_color='black'):
        self._center = center
        self.__out_color = out_color

    def move_center(self, new_coords):
        self._center = new_coords

