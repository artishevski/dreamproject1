from tkinter import *
from Shapes.Line import *
from GUI.FigureDrawing.EllipseDrawing import *
class MainScreen:
    def __init__(self):
        window = Tk()
        window.title("dreamproject1")
        window.geometry('800x500+400+150')

        self.canvas = Canvas()
        menu = Menu(window)
        figure_choser = Menu(menu, tearoff = 0)
        figure_choser.add_command(label = 'line', command = self.line)
        figure_choser.add_command(label = 'half line')
        figure_choser.add_command(label = 'interval')
        figure_choser.add_command(label = 'triangle')
        figure_choser.add_command(label = 'rectangle')
        figure_choser.add_command(label = 'diamond')
        figure_choser.add_command(label = 'equilateral triangle')
        figure_choser.add_command(label = 'square')
        figure_choser.add_command(label = 'equilateral pentagon')
        figure_choser.add_command(label = 'equilateral hexagon')
        figure_choser.add_command(label = 'ellipse')
        figure_choser.add_command(label = 'circle')
        menu.add_cascade(label = 'Choose a figure', menu = figure_choser)

        out_color_choser = Menu(menu, tearoff = 0)
        menu.add_cascade(label = 'Out color', menu =  out_color_choser)

        filling_color_choser = Menu(menu, tearoff = 0)
        menu.add_cascade(label = 'Filling color', menu = filling_color_choser)

        window.config(menu = menu)

        self.canvas.create_polygon([-30,-40,120,80], outline = 'black', width = 5)
        self.canvas.pack(fill=BOTH)

        a=EllipseDrawing()
        a.draw_shape(self.canvas, [60, 60, 200, 150, "blue", "red"])
        window.mainloop()

    def line(self):
        self.shape = Line()