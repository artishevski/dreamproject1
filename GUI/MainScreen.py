from tkinter import *
from shapes.Shape import Shape
from shapes.polygon_shape.PolygonShape import PolygonShape
from shapes.oval_shape.OvalShape import OvalShape
#from shapes.polygon_shape.Line import Line
#from shapes.polygon_shape.Halfline import Halfline
#from shapes.polygon_shape.Interval import Interval
from shapes.polygon_shape.Triangle import Triangle
from shapes.polygon_shape.Rectangle import Rectangle
from shapes.polygon_shape.Diamond import Diamond
from shapes.polygon_shape.Square import Square
#from shapes.oval_shape.Pentagon import Circle
from shapes.oval_shape.Ellipse import Ellipse
from shapes.oval_shape.Circle import Circle
from shapes.Point import Point


class MainScreen:

    def __init__(self):
        window = Tk()
        window.title("dreamproject1")
        window.geometry('800x500+400+150')
        self.shape = Shape()
        self.menu = Menu(window)
        figure_choser = Menu(self.menu, tearoff=0)
        figure_choser.add_command(label='line', command=self.line)
        figure_choser.add_command(label='half line', command=self.halfline)
        figure_choser.add_command(label='interval', command=self.interval)
        figure_choser.add_command(label='triangle', command=self.triangle)
        figure_choser.add_command(label='rectangle', command=self.rectangle)
        figure_choser.add_command(label='diamond', command=self.diamond)
        figure_choser.add_command(label='square', command=self.square)
        figure_choser.add_command(label='pentagon', command=self.pentagon)
        figure_choser.add_command(label='ellipse', command=self.ellipse)
        figure_choser.add_command(label='circle', command=self.circle)
        self.menu.add_cascade(label='Choose a figure', menu=figure_choser)

        out_color_choser = Menu(self.menu, tearoff=0)
        out_color_choser.add_command(label = 'red', command = self.out_red)
        out_color_choser.add_command(label = 'blue', command = self.out_blue)
        out_color_choser.add_command(label = 'green', command = self.out_green)
        out_color_choser.add_command(label = 'yellow', command = self.out_yellow)
        out_color_choser.add_command(label = 'black', command = self.out_black)
        self.menu.add_cascade(label='Out color', menu=out_color_choser)

        filling_color_choser = Menu(self.menu, tearoff=0)
        filling_color_choser.add_command(label = 'red', command = self.in_red)
        filling_color_choser.add_command(label = 'blue', command = self.in_blue)
        filling_color_choser.add_command(label = 'green', command = self.in_green)
        filling_color_choser.add_command(label = 'yellow', command = self.in_yellow)
        filling_color_choser.add_command(label = 'black', command = self.in_black)
        self.menu.add_cascade(label='Filling color', menu=filling_color_choser)

        window.config(menu=self.menu)

        self.canvas = Canvas()
        #self.canvas.create_polygon([-30, -40, 120, 80], outline='black', width=8)
        self.canvas.pack(fill=BOTH)

        self.canvas.bind('<Button-1>', self.popup)

        #a = EllipseDrawing()
        #a.draw_shape(self.canvas, [60, 60, 200, 150, "blue", "red"])
        window.mainloop()

    def popup(self, event):
        if isinstance(self.shape, OvalShape):
            self.shape.move_center(Point(event.x, event.y))
            self.canvas.create_oval(self.shape._top_left_coord._x, self.shape._top_left_coord._y,
                                    self.shape._bottom_right_coord._x, self.shape._bottom_right_coord._y,
                                    outline = self.shape._out_color, fill =self.shape._in_color, width = 8)
        if isinstance(self.shape, PolygonShape):
            self.shape.move_center(Point(event.x, event.y))
            self.canvas.create_polygon([(p._x, p._y) for p in self.shape._border_coords],
                                       outline = self.shape._out_color, fill =self.shape._in_color, width = 8)

    def line(self):
        #to-do
        pass

    def halfline(self):
        #to-do
        pass

    def interval(self):
        #to-do
        pass

    def triangle(self):
        self.shape = Triangle()

    def rectangle(self):
        self.shape = Rectangle()

    def diamond(self):
        self.shape = Diamond()

    def square(self):
        self.shape = Square()

    def pentagon(self):
        self.shape = Circle(radius=30)

    def ellipse(self):
        self.shape = Ellipse()

    def circle(self):
        self.shape = Circle(radius=30)

    def out_red(self):
        self.shape._out_color = 'red'

    def out_blue(self):
        self.shape._out_color = 'blue'

    def out_green(self):
        self.shape._out_color = 'green'

    def out_yellow(self):
        self.shape._out_color = 'yellow'

    def out_black(self):
        self.shape._out_color = 'black'

    def in_red(self):
        self.shape._in_color = 'red'

    def in_blue(self):
        self.shape._in_color = 'blue'

    def in_green(self):
        self.shape._in_color = 'green'

    def in_yellow(self):
        self.shape._in_color = 'yellow'

    def in_black(self):
        self.shape._in_color = 'black'