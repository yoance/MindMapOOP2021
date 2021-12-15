from tkinter import *

class button:
    def __init__(self, master, texts, sizex, posx, posy, comms):
        self.myButton = Button(master,text=texts, padx = sizex, command = comms)
        self.myButton.place(relx=posx, rely=posy)
    def setText (self, text):
        self.myButton.config(text=text)
    def setHeight (self, height):
        self.myButton.config(height=height)
    def setWidth (self, width):
        self.myButton.config(width=width)