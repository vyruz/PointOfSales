from MenuItemSubClass import *
class Order:
    #__items = [] #list of menu items on the order
    def __init__(self, ID):
        self.orderID = ID
        self.__items = [] 

    # returns total cost of bill, including tax
    def calculateBill(self):
        total = 0
        tax = 1.08
        for item in self.__items:
            total += item.getPrice()
        return total * tax 

    def addItem(self, item):
        self.__items.append(item)

    def removeItem(self, item):
        self.__items.remove(item)

    def removeItemIndex(self, index):
        del self.__items[index]

    def getItems(self):
        return self.__items

    def getID(self):
        return self.orderID

    def printItems(self):
        #instead of printing, concatenate a string
        output = "Order " + self.getID() + ":\n"
        #print output #"Order", self.getID(),":"
        for item in self.getItems():
            if(isinstance(item, FoodItem)):
                output = output+ "   "+item.__class__.__name__+" - "+item.getName()+" - $"+str(item.getPrice())+"\n"
                if(item.getComments()!=""):
                    output = output+"          "+item.getComments()+"\n"
            if(isinstance(item, DrinkItem)):
                output = output+"   "+"Drink"+" - "+item.getName()+" - $"+str(item.getPrice())+"\n"
                if(item.getComments()!=""):
                    output = output+"          "+item.getComments()+"\n"
        return output

    def split(self, num):
        if num > 0:
            return self.calculateBill() / num
        else:
            return self.calculateBill()

