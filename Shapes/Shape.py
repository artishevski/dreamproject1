from typing import Any
from GUI.FigureDrawing.ShapeDrawing import *

class Shape:
    def __init__(self, center = 8, out_color = 'black'):
        self._center = center
        self.__out_color = out_color
        self.__painter = ShapeDrawing()

    def __draw_figure__(self, canvas, info = None):
        self.__painter.draw_shape(canvas, info)

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)

