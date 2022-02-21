from tkinter import *

class MainScreen:
    def __init__(self):
        window = Tk()
        window.title("dreamproject1")
        window.geometry('800x500+400+150')

        menu = Menu(window)
        figure_choser = Menu(menu, tearoff = 0)
        figure_choser.add_command(label = 'line')
        figure_choser.add_command(label = 'half line')
        figure_choser.add_command(label = 'interval')
        figure_choser.add_command(label = 'triangle')
        figure_choser.add_command(label = 'rectangle')
        figure_choser.add_command(label = 'diamond')
        figure_choser.add_command(label = 'equilateral triangle')
        figure_choser.add_command(label = 'square')
        figure_choser.add_command(label = 'equilateral pentagon')
        figure_choser.add_command(label = 'equilateral hexagon')
        figure_choser.add_command(label = 'ellipsis')
        figure_choser.add_command(label = 'circle')
        menu.add_cascade(label = 'Choose a figure', menu = figure_choser)

        out_color_choser = Menu(menu, tearoff = 0)
        menu.add_cascade(label = 'Out color', menu = out_color_choser)

        filling_color_choser = Menu(menu, tearoff = 0)
        menu.add_cascade(label = 'Filling color', menu = filling_color_choser)

        window.config(menu = menu)

        canvas = Canvas()
        canvas.create_polygon([30,40,120,80], outline = 'black', width = 5)
        canvas.pack(fill=BOTH)
        window.mainloop()