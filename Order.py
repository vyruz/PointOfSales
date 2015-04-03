from MenuItemSubClass import *
class Order:
    #__items = [] #list of menu items on the order
    def __init__(self, ID):
        self.orderID = ID
        self.__items = [] 
    # returns total cost of bill, including tax
    def calculateBill(self):
        total = 0
        tax = 1
        for item in self.__items:
            total += item.getPrice()
        return total * tax 

    def addItem(self, item):
        #Adding an item to one order adds it to an other one. 
        self.__items.append(item)
    def removeItem(self, item):
        self.__items.remove(item)
    def getItems(self):
        return self.__items
    def getID(self):
        return self.orderID
    def printItems(self):
        print "Order", self.getID(),":"
        for item in self.getItems():
            if(isinstance(item, FoodItem)):
                print "   ",item.__class__.__name__,"-",item.getName(),"- $"+str(item.getPrice())
                if(item.getComments()!=""):
                    print"          ",item.getComments()
            if(isinstance(item, DrinkItem)):
                print "   ","Drink","-",item.getName(),"- $"+str(item.getPrice())
                if(item.getComments()!=""):
                    print "          ",item.getComments()

    def split(self, num):
        if num > 0:
            return self.calculateBill() / num
        else:
            return self.calculateBill()

