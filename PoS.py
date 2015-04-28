from Tkinter import *
from MenuItemSubClass import *
from Order import *
#from Test import *
from UserClass import *
import tkMessageBox


class App:	

	def __init__(self):
		#create the user. Orders will be associated with/stored in this user
		self.user = User()

		master = Tk()
		master.title("Point Of Sales")
		frame = Frame(master, bd = 100)
		frame.pack()

		Label (frame, text = "Order Number").grid(row=2)

		self.e1 = Entry(frame)
		self.e1.grid(row=2, column=1)

		Button(frame,text='Quit', command = frame.quit).grid(row = 3, column = 0, sticky=W, pady = 3)
		#Create a new order for the user and open a window to edit it
		Button(frame,text='Create New Order',command = self.newOrder).grid(row=4,column=1, sticky=W,pady=3)
		#Edit an order that's already been created
		Button(frame,text='Edit Existing Order',command = self.editOrder).grid(row=5,column=1,sticky=W,pady=3)

		master.mainloop()

	def newOrder(self):
		orderID = self.e1.get()
		order = self.user.getOrder(orderID)
		#check if there's already an order with this ID
		if(order == None):
			#add order to user's list of orders
			order = self.user.createOrder(orderID)
			self.orderWindow(order)
		#if this order already exists, ask if user wants to edit or go back
		else:
			self.editPromptWindow(order)

	def editOrder(self):
		orderID = self.e1.get()
		order = self.user.getOrder(orderID)
		#check if there is already an order with this ID
		if(order == None):
			#create a new order to edit
			newOrder = self.user.createOrder(orderID)
			self.newPromptWindow(newOrder)
		else:
			#edit an existing order
			self.orderWindow(order)

	def editPromptWindow(self, order):
		root = Tk()
		root.title("Order Already Exists")

		Label(root, text = "An order with this number already exists.").grid(row=0)
		Label(root, text = "Would you like to edit the existing order?").grid(row=1)

		Button(root, text = "Edit", command = lambda: self.orderWindow(order)).grid(row=3)
		Button(root, text = "Close", command = root.destroy).grid(row = 4)

	def newPromptWindow(self, order):
		root = Tk()
		root.title("Order Does Not Exist")

		Label(root, text = "An order with this number does not exist.").grid(row=0)
		Label(root, text = "Would you like to create a new order?").grid(row=1)

		Button(root, text = "Create new order", command = lambda: self.orderWindow(order)).grid(row=3)
		Button(root, text = "Close", command = root.destroy).grid(row = 4)

	def orderWindow(self, order):
		root = Tk()
		
		#get the order number from e1 to put in the title
		title = "Order " + str(self.e1.get())
		root.title(title)
		root.geometry("720x400")

		#make a listbox to display live list of order
		listbox = Listbox(root, selectmode = EXTENDED)
		listbox.grid(row = 0, column = 1, columnspan = 2, sticky = E+W)


		#add comment text box

		Label(root, text = "\n \n \n Comments: ").grid(row = 0, column = 3, sticky = N)
		comBox = Entry(root)
		comBox.grid(row = 0, column = 3)

		#populate the listbox
		for item in order.getItems():
			listItem = item.getName() + " - $" + str(item.getPrice()) + " - " + item.getComments()
			listbox.insert(END, listItem)

		#create items to be added to order
		#this should be done with a flyweight or something
		banzaiBurger = Entre("Banzai Burger", 9, "", False, False)
		whiskeyBurger = Entre("Whiskey River BBQ Burger", 7, "", False, False)
		shroomBurger = Entre("Mushroom Swiss Burger", 8, "", False, False)
		baconBurger = Entre("Bacon Cheeseburger", 6, "", False, False)

		fries = Appetizer("Fries", 3, "", False, False)
		onionRings = Appetizer("Onion Rings", 3, "", False, False)
		chips = Appetizer("Chips & Salsa", 3, "", False, False)
		chili = Appetizer("Chili", 3, "", False, False)

		coke = SoftDrink("Coke", 2, "")
		drPepper = SoftDrink("Dr Pepper", 2, "")
		sprite = SoftDrink("Sprite", 2, "")
		rootBeer = SoftDrink("Root Beer", 2, "")
		lemonade = SoftDrink("Freckled Lemonade", 4, "")

		beerShake = HardDrink("Irish Beer Shake", 6, 5, "")
		baileysShake = HardDrink("Baileys Irish Cream Shake", 6, 5, "")
		beerRita = HardDrink("Beer Rita", 7, 10, "")

		#sorry
		#food items
		E1 = Button(root, text = banzaiBurger.getName(), command = lambda: self.addComment(order, banzaiBurger, comBox, listbox)).grid(row = 2, column = 0, sticky = E+W)
		E2 = Button(root, text = whiskeyBurger.getName(), command = lambda: self.addComment(order, whiskeyBurger, comBox, listbox)).grid(row = 3, column = 0, sticky = E+W)
		E3 = Button(root, text = shroomBurger.getName(), command = lambda: self.addComment(order, shroomBurger, comBox, listbox)).grid(row = 4, column = 0, sticky = E+W)
		E4 = Button(root, text = baconBurger.getName(), command = lambda: self.addComment(order, baconBurger, comBox, listbox)).grid(row = 5, column = 0, sticky = E+W)

		A1 = Button(root, text = fries.getName(), command = lambda: self.addComment(order, fries, comBox, listbox)).grid(row = 2, column = 1, sticky = E+W)
		A2 = Button(root, text = onionRings.getName(), command = lambda: self.addComment(order, onionRings, comBox, listbox)).grid(row = 3, column = 1, sticky = E+W)
		A3 = Button(root, text = chips.getName(), command = lambda: self.addComment(order, chips, comBox, listbox)).grid(row = 4, column = 1, sticky = E+W)
		A4 = Button(root, text = chili.getName(), command = lambda: self.addComment(order, chili, comBox, listbox)).grid(row = 5, column = 1, sticky = E+W)

		S1 = Button(root, text = coke.getName(), command = lambda: self.addComment(order, coke, comBox, listbox)).grid(row = 2, column = 2, sticky = E+W)
		S2 = Button(root, text = drPepper.getName(), command = lambda: self.addComment(order, drPepper, comBox, listbox)).grid(row = 3, column = 2, sticky = E+W)
		S3 = Button(root, text = sprite.getName(), command = lambda: self.addComment(order, sprite, comBox, listbox)).grid(row = 4, column = 2, sticky = E+W)
		S4 = Button(root, text = rootBeer.getName(), command = lambda: self.addComment(order, rootBeer, comBox, listbox)).grid(row = 5, column = 2, sticky = E+W)
		S5 = Button(root, text = lemonade.getName(), command = lambda: self.addComment(order, lemonade, comBox, listbox)).grid(row = 6, column = 2, sticky = E+W)

		H1 = Button(root, text = beerShake.getName(), command = lambda: self.addComment(order, beerShake, comBox, listbox)).grid(row = 2, column = 3, sticky = E+W)
		H2 = Button(root, text = baileysShake.getName(), command = lambda: self.addComment(order, baileysShake, comBox, listbox)).grid(row = 3, column = 3, sticky = E+W)
		H3 = Button(root, text = beerRita.getName(), command = lambda: self.addComment(order, beerRita, comBox, listbox)).grid(row = 4, column = 3, sticky = E+W)

		#remove items, get the total cost in a pop up window or close the window
		C = Button(root, text = 'Calculate Bill', command = lambda: self.calcBill(order)).grid(row = 0, column = 0, sticky = E)
		R = Button(root, text = "Remove", command = lambda: self.deleteItem(order, listbox)).grid(row = 0, column = 0, sticky = W)
		Cl = Button(root, text = "Close", command = root.destroy).grid(row = 0, column = 0, sticky = N)

	def addComment(self, order, item, comBox, listbox):
		#actually add the comment, then close the window
		item.setComments(comBox.get())
		self.addItem(order, item, listbox)
		comBox.delete(0, "end")

	def addItem(self, order, item, listbox):
		#add to order
		order.addItem(item)

		#add to listbox
		listItem = item.getName() + " - $" + str(item.getPrice()) + " - " + item.getComments()
		listbox.insert(END, listItem)


	def deleteItem(self, order, listbox):
	    
	    #remove from listbox
	    items = listbox.curselection()
	    pos = 0
	    for i in items :
	        index = int(i) - pos
	        listbox.delete( index,index )
	        #self.order.removeItemIndex(index)
	        order.removeItemIndex(index)
	        pos += 1

	def calcBill(self, order):
		#used when order is complete, shows total and removes order from list
		#total = "$" + str(self.order.calculateBill())
		total = "$" + str(order.calculateBill())
		tkMessageBox.showinfo("Bill", total)

		#user.removeOrder(order.getID())


app = App()