from shapes.Point import Point
from shapes.polygon_shape.PolygonShape import PolygonShape

class Diamond(PolygonShape):
    def __init__(self, center=Point(0, 0), diam=90, out_color='red', in_color='blue'):
        super().__init__(center, None, out_color, in_color)
        self._diam = diam

    def move_center(self, new_coords: Point):
        super(Diamond, self).move_center(new_coords)
        top_left_coord = Point(self._center._x, self._center._y - self._diam/2)
        bottom_left_coord = Point(self._center._x - self._diam / 3, self._center._y)
        top_right_coord = Point(self._center._x, self._center._y + self._diam / 2)
        bottom_right_coord = Point(self._center._x + self._diam/3, self._center._y)
        self._border_coords = [top_left_coord, bottom_left_coord, top_right_coord,  bottom_right_coord]