from abc import ABC, abstractmethod
class Shape(ABC):

	def Concrete(self):
		print(f"I am not abstract method")

	@abstractmethod
	def area(self):  # make it an abstsract method by @abstarctmethod
		pass
	@abstractmethod
	def perimeter(self):
		pass

class Square(Shape):
	def __init__(self, side):
		self.__side = side

	def area(self):  # redefine by removing abstract method
		return self.__side * self.__side

	def perimeter(self):
		return 4 * self.__side

#obj = Shape()  # will gives error you cannot creat eabject for abstract class

obj1 = Square(4)
print("Area: ", obj1.area())
print("Perimeter: ", obj1.perimeter())
obj1.Concrete()  # don't need to redefine this since it is not abstract