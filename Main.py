from functools import partial
from Node import *
from Edge import *
from ObjectManager import *
from MainConsole import *

from tkinter import *
from Button import *
from Entry import *
from ObjectUI import *

from tkinter.colorchooser import askcolor
import math


def close_winc(top):
   x0, y0, x1, y1 = cnv.coords(cnv.selected)
   cnv.coords(cnv.selected, x0, y0, x0+2*rad_entry, y0+2*rad_entry)
   cnv.itemconfig(cnv.selected, fill=col_button)
   top.destroy()

def close_wino(top): #used to config ovals and rectangles
   x0, y0, x1, y1 = cnv.coords(cnv.selected)
   cnv.coords(cnv.selected, x0, y0, x0+2*hrad_entry, y0+2*vrad_entry)
   cnv.itemconfig(cnv.selected, fill=col_button)
   top.destroy()

def close_winl(top):
   x0, y0, x1, y1 = cnv.coords(cnv.selected)
   cnv.coords(cnv.selected, x0, y0, math.sqrt(2)*rad_entry, math.sqrt(2)*rad_entry)
   top.destroy()

def choose_color():
    color_code = colorchooser.askcolor(title ="Choose color")
    return(color_code)

def popupc():
   top= Toplevel(myFrame)
   top.geometry("750x250")
   rad_label = Label(root, text="Radius")
   rad_label.pack()
   rad_entry= Entry(top, width= 10)
   rad_entry.pack()
   col_button = Button(root, text = "Select color", command = choose_color)
   col_button.pack()
   button= Button(top, text="Ok", command=lambda:close_winc(top))
   button.pack(pady=5, side= TOP)

def popupo():
   top= Toplevel(myFrame)
   top.geometry("750x250")
   hrad_label = Label(root, text="Horizontal Radius")
   hrad_label.pack()
   hrad_entry= Entry(top, width= 10)
   hrad_entry.pack()
   vrad_label = Label(root, text="Vertical Radius")
   vrad_label.pack()
   vrad_entry= Entry(top, width= 10)
   vrad_entry.pack()
   col_button = Button(root, text = "Select color", command = choose_color)
   col_button.pack()
   button= Button(top, text="Ok", command=lambda:close_wino(top))
   button.pack(pady=5, side= TOP)

def popupr():
   top= Toplevel(myFrame)
   top.geometry("750x250")
   hrad_label = Label(root, text="Width")
   hrad_label.pack()
   hrad_entry= Entry(top, width= 10)
   hrad_entry.pack()
   vrad_label = Label(root, text="Height")
   vrad_label.pack()
   vrad_entry= Entry(top, width= 10)
   vrad_entry.pack()
   col_button = Button(root, text = "Select color", command = choose_color)
   col_button.pack()
   button= Button(top, text="Ok", command=lambda:close_wino(top))
   button.pack(pady=5, side= TOP)

def popupl():
   top= Toplevel(myFrame)
   top.geometry("750x250")
   rad_label = Label(root, text="Length")
   rad_label.pack()
   rad_entry= Entry(top, width= 10)
   rad_entry.pack()
   col_button = Button(root, text = "Select color", command = choose_color)
   col_button.pack()
   button= Button(top, text="Ok", command=lambda:close_winl(top))
   button.pack(pady=5, side= TOP)

#Event Listeners
def on_click(event):
    selected = cnv.find_overlapping(event.x-10, event.y-10, event.x+10, event.y+10)
    if selected:
        cnv.selected = selected[-1]  # select the top-most item
        cnv.startxy = (event.x, event.y)

        global selectedObj, prevSelectedObj
        prevSelectedObj = selectedObj #for making lines        
        selectedObj = cnv.selected - tkObjectID # sync objectID
        #print(searchNodeID(prevSelectedObj).getName())

        if(searchNodeID() != False):
            input.set_text(searchNodeID().getName())
        
        lineButton.setHeight(10)
        lineButton.setWidth(4)
        lineButton.setText(str("Line:\nConnect to\n" + searchNodeID(prevSelectedObj).getName()))
        # print(cnv.selected)
        # print(searchNodeID().getName())
        # print(cnv.selected, cnv.startxy)
    # else:
    #     cnv.selected = None

def on_drag(event):
    if cnv.selected:
        # calculate distance moved from last position
        dx, dy = event.x-cnv.startxy[0], event.y-cnv.startxy[1]
        # move the selected item
        cnv.move(cnv.selected, dx, dy)
        # update last position
        cnv.startxy = (event.x, event.y)

def double_click(event):
    selected = cnv.find_overlapping(event.x-10, event.y-10, event.x+10, event.y+10)
    if selected:
        cnv.selected = selected[-1]    
    if searchNodeID().objectType == "circle":
        popupc()
    if searchNodeID().objectType == "oval":
        popupo()
    if searchNodeID().objectType == "rectangle":
        popupr()
    if searchNodeID().objectType == "line":
        popupl()


#Functions
def deleteAll():
    #cnv.pack_forget()
    cnv.delete(ALL)
    inputEntry(input.myEntry)

    for i in nodeList:
        objMgr.removeObject(i.getObjectID())
    for i in edgeList:
        objMgr.removeObject(i.getObjectID())

    nodeList.clear()
    edgeList.clear()

    global tkObjectID 
    tkObjectID = tkObjectID + 1 #Sync tkinter object ID with ObjectManager object ID
    input.set_text("")

def deleteSelected():
    cnv.delete(cnv.selected)
    if not nodeList:
        nodeList.remove(searchNodeID())

        for i in edgeList:
            if i.getObjectID() == selectedObj or i.getNode1() == selectedObj or i.getNode2() == selectedObj :
                cnv.remove(i.getObjectID()+tkObjectID)
                objMgr.removeObject(i.getObjectID())
                edgeList.remove(i)
        input.set_text("")
    # print(nodeList) 

def inputEntry(entry):
    cnv.create_window(300, 450, window=entry, width=400)
    cnv.pack()

def createObject(type):
    objMgr.newObject()
    if(type == "circle"):
        objUI.circle()
    elif(type == "oval"):
        objUI.oval()
    elif(type == "rectangle"):
        objUI.rectangle()
    nodeList.append(Node(objMgr.getLatestObjectID(),objectType=type))
    
def createEdge():
    global prevSelectedObj, selectedObj, tkObjectID
    
    if(len(nodeList)>=2 and prevSelectedObj != selectedObj):
        objMgr.newObject()
        edgeList.append(Edge(objMgr.getLatestObjectID(), searchNodeID(prevSelectedObj).getObjectID(), searchNodeID().getObjectID()))
        x0, y0, x1, y1 = cnv.coords(prevSelectedObj+tkObjectID)
        node1_x = (x0+x1)/2
        node1_y = (y0+y1)/2
        
        x0, y0, x1, y1 = cnv.coords(selectedObj+tkObjectID)
        node2_x = (x0+x1)/2
        node2_y = (y0+y1)/2
        objUI.line(node1_x, node1_y, node2_x, node2_y)
        
        if(len(edgeList) == len(edgeList)-1):
            input.set_text("Previously and Currently selected objects must be Nodes!")
        else:
            input.set_text(searchNodeID(prevSelectedObj).getName() + " is now connected to " + searchNodeID().getName())
    elif(len(nodeList)<2):
        input.set_text("There must be at least 2 Nodes!")
    else:
        input.set_text("Previously and Currently selected Nodes must be different!")

def searchNodeID(id=0):
    if (id == 0):
        for i in nodeList:
            global selectedObj
            if i.getObjectID() == selectedObj:
                return i
    else:
        for i in nodeList:
            if i.getObjectID() == id:
                return i
    return False

def renameNode():
    searchNodeID().setName(input.get_text())

def startConsole():
    input.set_text("Starting Console!")
    console = MainConsole()
    global nodeList, edgeList
    nodeList, edgeList = console.startConsole(nodeList, edgeList)
    input.set_text("Console Stopped!")


#Preparing Tkinter Frame and Canvas for UI
root = Tk()
root.title("Mind Map Maker")
root.geometry("800x500")

myFrame = Frame(root)
cnv = Canvas(root, height = 500, width = 600, background = "#00f2da")
cnv.pack()

cnv.bind("<Button-1>", on_click)
cnv.bind("<B1-Motion>", on_drag)
cnv.bind('<Double-1>', double_click)

objUI = ObjectUI(cnv)
input = entry(root)
inputEntry(input.myEntry)


#Preparing Variables to Store Values
nodeList = []
edgeList = []
objMgr = ObjectManager()
tkObjectID = 1 #Sync tkinter object ID with ObjectManager object ID
prevSelectedObj = 1
selectedObj = 1

exitButton = button(root, "Exit", 20, 0, 0, exit)
circleButton = button(root, "Circle", 20, 0.885, 0, partial(createObject, "circle"))
ovalButton = button(root, "Oval", 23, 0.885, 0.07, partial(createObject, "oval"))
rectangleButton = button(root, "Rectangle", 9, 0.885, 0.14, partial(createObject, "rectangle"))
lineButton = button(root, 'Line', 21, 0.885, 0.21, createEdge)
consoleButton = button(root, 'Console', 14, 0.885, 0.60, startConsole)
enterButton = button(root, 'Enter', 24, 0.885, 0.87, renameNode)
deleteSelectedButton = button(root, 'Delete', 28, 0, 0.40, deleteSelected)
deleteButton = button(root, 'Delete All', 19, 0, 0.50, deleteAll)

root.mainloop()