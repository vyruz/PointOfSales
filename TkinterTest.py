from Tkinter import *
from MenuItemSubClass import *
from Order import *
#from Test import *
from UserClass import *
import tkMessageBox


user = User()
#order = None

def orderWindow(order):
	root = Tk()
	
	#get the order number from e1 to put in the title
	title = "Order",e1.get()
	root.title(title)

	frame1 = Frame(root, bd = 100)
	frame1.pack()
	
	#create items to be added to order
	#this should be done with a flyweight or something
	burrito = Entree("Burrito", 6, "Guac", False, False)
	burger = Entree("Burger", 8, "Medium", False, False)
	coke = SoftDrink("Coke", 2, "No Ice")

	#food items
	F1 = Button(root, text = 'Burrito', command = lambda: addItem(order, burrito))
	F2 = Button(root, text = "Burger", command = lambda: addItem(order, burger))
	D1 = Button(root, text = "Coke", command = lambda: addItem(order, coke))

	#view the order or the total cost in a pop up window
	C = Button(root, text = 'View Order', command = lambda: viewOrder(order))
	D = Button(root, text = 'Calculate Bill', command = lambda: calcBill(order))
	
	#some tkinter thing that I guess should be done
	F1.pack()
	F2.pack()
	D1.pack()
	C.pack()
	D.pack()

def editPromptWindow(order):
	root = Tk()
	root.title("Order Already Exists")

	Label(root, text = "An order with this number already exists.").grid(row=0)
	Label(root, text = "Would you like to edit the existing order?").grid(row=1)
	Label(root, text = "If not, just close this window.").grid(row=2)

	Button(root, text = "Edit", command = lambda: orderWindow(order)).grid(row=4)

def newPromptWindow(order):
	root = Tk()
	root.title("Order Does Not Exist")

	Label(root, text = "An order with this number does not exist.").grid(row=0)
	Label(root, text = "Would you like to create a new order?").grid(row=1)
	Label(root, text = "If not, just close this window.").grid(row=2)

	Button(root, text = "Create new order", command = lambda: orderWindow(order)).grid(row=4)

def newOrder():
	orderID = e1.get()
	order = user.getOrder(orderID)
	#check if there's already an order with this ID
	if(order == None):
		#add order to user's list of orders
		order = user.createOrder(orderID)
		orderWindow(order)
	#if this order already exists, ask if user wants to edit or go back
	else:
		editPromptWindow(order)
	

def editOrder():
	orderID = e1.get()
	order = user.getOrder(orderID)
	#check if there is already an order with this ID
	if(order == None):
		#create a new order to edit
		newOrder = user.createOrder(orderID)
		newPromptWindow(newOrder)
	else:
		#edit an existing order
		orderWindow(order)

def addItem(order, item):
	order.addItem(item)

def viewOrder(order):
	tkMessageBox.showinfo("Order", order.printItems())

def calcBill(order):
	total = "$",order.calculateBill()
	tkMessageBox.showinfo("Bill", total)

master = Tk()
master.title("Point Of Sales")
frame = Frame(master, bd = 100)
frame.pack()

#have to figure out formatting so this text doesn't look like crap
#Label(frame, text = "Enter a new order number to create a new order or an").grid(row=0, column=1)
#Label(frame, text = "existing order number to edit that order").grid(row=1, column=1)

Label (frame, text = "Order Number").grid(row=2)

e1 = Entry(frame)
e1.grid(row=2, column=1)

Button(frame,text='Quit', command = frame.quit).grid(row = 3, column = 0, sticky=W, pady = 3)
#Create a new order for the user and open a window to edit it
Button(frame,text='Create New Order',command=newOrder).grid(row=4,column=1, sticky=W,pady=3)
#Edit an order that's already been created
Button(frame,text='Edit Existing Order',command=editOrder).grid(row=5,column=1,sticky=W,pady=3)

master.mainloop()