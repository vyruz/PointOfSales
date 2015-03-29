class MenuItem:
	def __init__ (self):
		self.name = "default name"
		self.price = "default price"
		self.avail = True
		self.comments = ""

	def getName(self):
		return self.name
	def setName(self,title):
		self.name = title

	def getPrice(self):
		return self.price
	def setPrice(self,cost):
		if (cost < 0):
			print "Invalid Price on ",self.getName()
			self.price = 0
		else:
			self.price = cost

	def getAvail(self):
		return self.avail
	def setAvailable(self):
		self.avail = True
	def setUnavailable(self):
		self.avail = False

	def getComments(self):
		return self.comments
	def setComments(self,text):
		self.comments = text
