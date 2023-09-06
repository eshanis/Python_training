#OVERLOAD CLASS METHODS
class Amazon:
	def __init__(self,name,price):
		self.name = name
		self.price = price

	def info(self):
		print(f"Product from info-Amazon: ")
		print(f"amazon product name: {self.name}")
		print(f"amazon product price: {self.price}")
class Flipkart:
	def __init__(self,name,price):
		self.name = name
		self.price = price
	def info(self):
		print(f"Product from info-Flipkart: ")
		print(f"flipkart product name: {self.name}")
		print(f"flipkart product price: {self.price}")

flp = Flipkart("iphone",150)
amz = Amazon("iphone",146)


for prod in (flp,amz): # pass product as tuple
	prod.info()