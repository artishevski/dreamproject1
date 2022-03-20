from shapes.Point import Point


class Shape:
    def __init__(self, center=Point(0, 0), out_color='blue', in_color ='blue'):
        self._center = center
        self._out_color = out_color
        self._in_color = in_color

    def move_center(self, new_coords: Point):
        self._center = new_coords

    def change_out_color(self, out_color):
        self._out_color = out_color

