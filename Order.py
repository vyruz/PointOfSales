class Order(orderID):
    __items = [] #list of menu items on the order

    # returns total cost of bill, including tax
    def calculateBill(self):
        total = 0
        tax = 1.09
        for item in self.__items:
            total += item.getPrice()
        return total * tax 

    def addItem(item):
        self.__items.append(item)
    def removeItem(item):
        self.items.remove(item)
    def split(num):
        if num > 0:
            return calculateBill() / num
        else:
            return calculateBill()
