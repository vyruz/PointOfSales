
class Order:
    __items = [] #list of menu items on the order
    def __init__(self, ID):
        self.orderID = ID

    # returns total cost of bill, including tax
    def calculateBill(self):
        total = 0
        tax = 1.09
        for item in self.__items:
            total += item.getPrice()
        return total * tax 

    def addItem(self, item):
        self.__items.append(item)
    def removeItem(self, item):
        self.__items.remove(item)
    def getItems(self):
        return self.__items
    def split(self, num):
        if num > 0:
            return self.calculateBill() / num
        else:
            return self.calculateBill()

