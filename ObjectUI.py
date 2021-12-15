from tkinter import *

class ObjectUI:
    def __init__(self, myCanvas):
        self.myCanvas = myCanvas
    def circle(self):
        self.myCanvas.create_oval(60,60,210,210,fill= "blue", outline="black")
        return
    def oval(self):
        self.myCanvas.create_oval(60,110,300,210,fill= "blue")
        return
    def rectangle(self):
        self.myCanvas.create_rectangle(30,30,150,190,fill= "blue")
        return
    def line(self, x0, y0, x1, y1):
        self.myCanvas.create_line(x0, y0, x1, y1, arrow = LAST)
        return

