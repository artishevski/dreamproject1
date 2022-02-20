from tkinter import *
from Shapes import Shape



window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
canvas = Canvas()
canvas.create_polygon([50,40,120,80], outline = 'black', width = 5)
canvas.pack(fill=BOTH)
#window.mainloop()

shape = Shape()
##print(shape.__getattribute__('center'))