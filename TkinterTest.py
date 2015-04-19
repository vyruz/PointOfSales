from Tkinter import *
from MenuItemSubClass import *
from Order import *
from Test import *
from UserClass import *
import tkMessageBox

def ShowEntry():
	tkMessageBox.showinfo("Show Order Number", "Order Number: %s" % (e1.get()))

def Open1():
	root = Tk()
	frame1 = Frame(root, bd = 100)
	frame1.pack()
	UserClass.CreateOrder()
	B=Button(root,text='Burrito', command=AddBurrito)
	C=Button(root,text='View Order', command=ViewOrder)
	B.pack()
	C.pack()

def AddBurrito():
	tkMessageBox.showinfo("","Burrito Added to Order")

def ViewOrder():
	tkMessageBox.showinfo("","The Order Contains: " + getItems())

def OpenMaster():
	master = Tk()
	frame = Frame(master, bd = 100)
	frame.pack()

	Label (frame, text = "Order Number").grid(row=0)

	e1 = Entry(frame)
	e1.grid(row=0, column=1)

	Button(frame, text='Quit', command = frame.quit).grid(row = 3, column = 0, sticky=W, pady = 3)
	Button(frame, text='Show', command = ShowEntry).grid(row=3,column=1, sticky=W, pady = 3)
	Button(frame, text='Open1',command= Open1).grid(row=4,column=1, sticky=W,pady=3)

	mainloop()

master = Tk()
frame = Frame(master, bd = 100)
frame.pack()

Label (frame, text = "Order Number").grid(row=0)

e1 = Entry(frame)
e1.grid(row=0, column=1)

Button(frame, text='Quit', command = frame.quit).grid(row = 3, column = 0, sticky=W, pady = 3)
Button(frame, text='Show', command = ShowEntry).grid(row=3,column=1, sticky=W, pady = 3)
Button(frame, text='Create New Order',command= Open1).grid(row=4,column=1, sticky=W,pady=3)

mainloop()