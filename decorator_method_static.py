#STATIC DECORATOR
#1. access only class attributes
#2.like a normal method static method, you have to explicitly call it like obj.methodName or className eg className.methodName("hi") with or without parameter
#3.usually not done using obj.methodName since not bound to object even though it works
#4. @staticmethod - implemented
#5.NOT bound to any instance of object
# USED: eg. logging info for all employees.
class Employee:
	count = 100  # class attribute so inside the class

	def get_info(self):  # non static method, reference of object (self) as one of the parameters
		self.var = 200  # attribute
		print("var: ", self.var)  # this is instance variable and cannot be accessed outsode of this method.
		print("count: ",
		      Employee.count)  # calling count by class name since it is a class attribute and outside the method

	@classmethod  # this is for decorator class
	def myclassmethod(self, msg):  # msg is local attribute/variable
		print("cnt in clas method: ", Employee.count)
		print("message is: ", msg)

	# print("var is: ", self.var) # this will give an error since var is an instance variable

	@staticmethod
	def mydecStatic(msg):  # never accepts parameters like self
		print("cnt from static method: ", Employee.count)
		print("msg from static: ", msg)


emp1 = Employee()
emp1.get_info()
emp1.myclassmethod("Hi from class")
Employee.mydecStatic("Hi from Static")