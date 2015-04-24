from MenuItemSubClass import *
from Order import *
from UserClass import *
item1 = Entree('Burrito',10,'Guac',True, True)
# #print item1.getName()
item2 = Appetizer('Sampler',5,'',True,True)
# #print item2.getPrice()
# item3 = SoftDrink('Water', 0,'')
# item4 = HardDrink("Pina Coloda",6,30,"Extra coconutty")
# item5 = HardDrink("Corona",4,15,"3 limes on bottle")
# item6=HardDrink("Corona",4,15,"2 limes on bottle")

# # Order tests
# order0 = Order(0)
# order1 = Order(1)
# order0.addItem(item1)
# order0.addItem(item1)
# order0.addItem(item3)
# order0.addItem(item4)
# order1.addItem(item5)
# order1.addItem(item6)

# def addThing(order):
# 	order.addItem(item1)

# addThing(order0)

#order0.printItems()




#print("|"*140)
#order0.printItems()
#order1.printItems()
#print ("Order 0 Total $" +str(order0.calculateBill()))
#print ("Order 1 Total $" +str(order1.calculateBill()))

user = User()
user.createOrder(1)
user.createOrder(2)
user.createOrder(3)

user.getOrder(2).addItem(item1)
user.getOrder(2).printItems()

user.getOrder(1).addItem(item2)
user.getOrder(1).printItems()
user.getOrder(4)