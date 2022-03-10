
from GUI.FigureDrawing.ShapeDrawing import *
from tkinter import *

class EllipseDrawing(ShapeDrawing):
    def draw_shape(self, canvas, info):
        canvas.create_oval(
            info[0], info[1], info[2], info[3], outline=info[4],
            fill=info[5], width=4
        )