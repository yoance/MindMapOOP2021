from tkinter import *

class entry:
    def __init__(self, root):
        self.myEntry = Entry(root, justify=CENTER, selectborderwidth=4)
    def set_text(self, text):
        self.myEntry.delete(0,END)
        self.myEntry.insert(0,text)
        return
    def get_text(self):
        return self.myEntry.get()