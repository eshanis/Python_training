#PREDEFINED METHODS

# DUNDER METHODS/ DOUBLE UNDERSCORE METHODS/ MAGIC METHODS

#__init__()  # non-static method

# similar to constructor
# constructor is a method
# invoked automatically as soon as we create an object

#below code gives error since get method is not initialized so use __init__(_
# class Circle:
# 	pi = 3.14
# 	def get(self): #if get method is used instead of init, it gives an error
# 		self.rad=int(input("enter radius"))
# 	def area(self):
# 		print("Area of circle: ", Circle.pi*self.rad**2)
#
# obj = Circle()
# obj.area()

print("++++++++++++++++++++++++")

class Circle:
	pi = 3.14
	#def get(self):  if get method is used instead of init, it gives an error
	def __init__(self):
		self.rad=int(input("enter radius: "))
		self.dia=int(input("enter dia: "))

	def area(self):
		print("Area of circle: ", Circle.pi*self.rad**2)

	def circum(self):
		print(" circumference of circle: ", Circle.pi * self.dia)

obj = Circle()
obj.area()
obj.circum()