# CLASS DECORATOR

# 1. access only class attributes
# like a normal method non static method, you have to explicitly call it like obj.methodName
# 3. @classmehod - implemented
# 4.bound to object

# var = "Emp Info"
class Employee:
	count = 100  # class attribute so inside the class

	def get_info(self):  #non static method, reference of object (self) as one of the parameters
		self.var = 200  # attribute
		print("var: ", self.var) #this is instance variable and cannot be accessed outside of this method.
		print("count: ",
		      Employee.count)  # calling count by class name since it is a class attribute and outside the method

	@classmethod  # this is for decorator class
	def myclassmethod(self, msg):  # msg is local attribute/variable
		print("cnt: ", Employee.count)
		print("message is: ", msg)
		# print("var is: ", self.var) # this will give an error since var is an instance variable


emp1 = Employee()
emp1.get_info()
emp1.myclassmethod("All okay")
