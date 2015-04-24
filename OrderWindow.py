#Trying to separate this out into its own class 
#to avoid spaghetti code. Not sure how to yet.
#So far this is unused.

from TkinterTest import *

class OrderWindow:

	def __init__(self):
		#"ID" will be whatever was in e1 in the main class
		self.root = Tk()
		self.listbox = Listbox(root, selectmode = EXTENDED)
		self.order = order

	def addItem(self, item):

	def removeItem(self, item):

	def addCommentWindow(self, item):

	def addComment(self, item):

	#def viewOrder(self, order):

	#def calcBill(self, order):

	def hideWindow(self):

	def showWindow(self):
