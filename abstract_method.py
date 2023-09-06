#ABSTRACT CLASS AND ABSTRACT METHOD

#features of abstract class and method
#ABSTRACT CLASS
#1. to implement import ABC model (abstract base class model)
#2. it has lots of abstract methods
#3. it has lots of abstract properties
#4. you can import ABC class or from abc import ABC, abstract method
#5. class has to be inherited from a predefined class called ABC
#6. abstract class acts like a template and you reuse it, abstract call cannot be called directly meaning you cannot creat an object for abstract class directly
#7 abstract class can contain abstract method, conrete methods (non-static methods)

#ABSTRACT METHOD
#1 implemented by @abstractmethod
#2 will have only declaration not definition so no body for it.
#3. IMPORTANT: all the inherited /derived classes should implement this abstract method if not it will throw an error

#Eg abstract class shape
#derived shape of square, cirlce, rectangle etc.

from abc import ABC, abstractmethod
class Shape(ABC):

	def Concrete(self):
		print(f"I am not abstract method")

	@abstractmethod  # make it an abstsract method by @abstarctmethod
	def area(self):
		pass

	@abstractmethod
	def perimeter(self):
		pass

class Square(Shape):
	def __init__(self, side):
		self.__side=side

#obj = Shape()  # will gives error you cannot creat eabject for abstract class

obj1 = Square(4) # error email "cannot instantiat eabstract class square"