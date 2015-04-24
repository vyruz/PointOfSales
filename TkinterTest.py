from Tkinter import *
from MenuItemSubClass import *
from Order import *
#from Test import *
from UserClass import *
import tkMessageBox

#This should all be shoved into a class called "App" or something generic

user = User()

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
	
def orderWindow(order):
	root = Tk()
	
	#get the order number from e1 to put in the title
	title = "Order " + str(e1.get())
	root.title(title)
	root.geometry("300x350")

	#make a listbox to display live list of order
	listbox = Listbox(root, selectmode = EXTENDED)
	listbox.pack()

	#populate the listbox
	for item in order.getItems():
		listItem = item.getName() + " - $" + str(item.getPrice()) + " - " + item.getComments()
		listbox.insert(END, listItem)

	R = Button(root, text = "Remove", command = lambda: deleteItem(order, listbox))
	R.pack()

	#create items to be added to order
	#this should be done with a flyweight or something
	burrito = Entre("Burrito", 6, "Guac", False, False)
	burger = Entre("Burger", 8, "Medium", False, False)
	coke = SoftDrink("Coke", 2, "No Ice")

	#food items
	F1 = Button(root, text = "Burrito", command = lambda: addCommentWindow(order, burrito, listbox))
	F2 = Button(root, text = "Burger", command = lambda: addCommentWindow(order, burger, listbox))
	D1 = Button(root, text = "Coke", command = lambda: addCommentWindow(order, coke, listbox))

	#view the order or the total cost in a pop up window
	C = Button(root, text = 'Calculate Bill', command = lambda: calcBill(order))
	
	#some tkinter thing that I guess should be done
	F1.pack()
	F2.pack()
	D1.pack()
	C.pack()

def addCommentWindow(order, item, listbox):
	#prompt for a comment to be added to the food item
	root = Tk()
	root.title("Add Comment")

	Label(root, text = "Would you like to add a comment to this item?").grid(row=0)
	comment = Entry(root)
	comment.grid(row=1)

	B = Button(root, text = "Add to Order", command = lambda: addComment(order, item, comment.get(), root, listbox)).grid(row=2)

def addComment(order, item, comment, root, listbox):
	#actually add the comment, then close the window
	item.setComments(comment)
	addItem(order, item, listbox)
	root.destroy()

def ViewOrder():
	tkMessageBox.showinfo("","The Order Contains: " % order.printItems())

def addItem(order, item, listbox):
	#add to order
	order.addItem(item)

	#add to listbox
	listItem = item.getName() + " - $" + str(item.getPrice()) + " - " + item.getComments()
	listbox.insert(END, listItem)

####################THIS ONLY REMOVES IT FROM THE LISTBOX, NOT THE ACTUAL ORDER. Don't know how to pass
####################in the item to be removed because the only way the user identifies the item to remove
####################is by highlighting it in the listbox, but they're only highlighting text, there's no
####################item associated with it
def deleteItem(order, listbox):
    #delete from order
    #order.removeItem(item)

    #remove from listbox
    items = listbox.curselection()
    pos = 0
    for i in items :
        index = int(i) - pos
        listbox.delete( index,index )
        pos += 1

def viewOrder(order):
	tkMessageBox.showinfo("Order", order.printItems())

def calcBill(order):
	#used when order is complete, shows total and removes order from list
	total = "$" + str(order.calculateBill())
	tkMessageBox.showinfo("Bill", total)

	user.removeOrder(order.getID())


#Here's where shit actually starts

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

#make live list of order. This should go in the order window
#listbox = Listbox(frame, selectmode = EXTENDED)
#listbox.grid(row=2, column=2)

Button(frame,text='Quit', command = frame.quit).grid(row = 3, column = 0, sticky=W, pady = 3)
#Create a new order for the user and open a window to edit it
Button(frame,text='Create New Order',command=newOrder).grid(row=4,column=1, sticky=W,pady=3)
#Edit an order that's already been created
Button(frame,text='Edit Existing Order',command=editOrder).grid(row=5,column=1,sticky=W,pady=3)

master.mainloop()