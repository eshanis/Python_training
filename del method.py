print("=== DEALLOCATION OF MEMORY ===")
# to be notified when an object is deleted eg when an employee leaves

#__del__()

class Circle:
	pi = 3.14

	def __init__(self):
		self.rad = int(input("enter radius: "))

	def area(self):
		print("Area of circle: ", Circle.pi * self.rad ** 2)

	def circum(self):
		print(" circumference of circle: ", 2 * Circle.pi * self.rad)

	def __del__(self):
		print(f"{type(self)} deleted")


obj = Circle()
obj.area()
obj.circum()
del obj
# obj.area() # this statement will now give error since obj is deleted