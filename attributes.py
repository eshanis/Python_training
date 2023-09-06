print("======= 1. CLASS attribute / STATIC ATTRIBUTE SAME FEATURES ===============")
#-they are declared inside a class
#-are shared by all the elements of the class
#-accessed with the help of className
#- Memory is shared by all instances of your class

class Employee:
	empName = "Sam" # class attribute declraed inside class
	empid = 1000  #class scope - initializing class attribute
	def get_info(self):  #non static method
		print("EmpName.get: ", Employee.empName)
		print("Empid.get: ", Employee.empid)

	def disp_info(self):
		print("EmpName.disp: ", Employee.empName)
		print("Empid.disp: ", Employee.empid)

emp1=Employee()
emp1.get_info()
emp1.disp_info()
print("EmpName: ", Employee.empName)
print("Empid: ", Employee.empid)

print("++++++++++++++++++++++++++++++++++++++")

class Employee:
	empid = 100  # common memory, this is not released

	def eID_Gen(self):
		Employee.empid+=1

	def disp_Id(self):
		print("Employee id: ", Employee.empid)

emp1 = Employee()
emp1.eID_Gen() # memory/stack released once performed.
emp1.disp_Id() # memory/stack released once performed.

emp2 = Employee()
emp2.eID_Gen() # memory/stack released once performed.
emp2.disp_Id() # memory/stack released once performed.

emp3 = Employee()
emp3.eID_Gen() # memory/stack released once performed.
emp3.disp_Id() # memory/stack released once performed.

print("===============LOCAL ATTRIBUTE ==========================")

# declared inside a method/ block of code
# local scope - access only within the method where declared
# accessed directly with attribute name


class Employee:

	def get_info(self):  # non static method
		empName = input("Enter Name (Local var):")
		empid = int(input("Enter EmpId: "))
		print("EmpName-get: ", empName)
		print("Empid-get: ", empid)

	def disp_info(self): #the local varibale will not work in this method will give error
		print("EmpName-disp: ", empName)
		print("Empid-disp: ", empid)


emp1 = Employee()
emp1.get_info()
# emp1.disp_info()  does not work here. gives error message

print("===============INSTANCE ATTRIBUTE ==========================")

# instance scope.
# instance memory is not shared.  separate memory created for each instance
# every object will have its own copy of attribute

class Employee:

	def get_info(self):  # non static method
		self.empName = input("Enter Name (Local var):")  # instance variable
		self.empid = int(input("Enter EmpId: "))
		print("EmpName-get: ", self.empName)
		print("Empid-get: ", self.empid)

	def disp_info(self):
		print("EmpName-disp: ", self.empName)
		print("Empid-disp: ", self.empid)


emp1 = Employee()
emp1.get_info()
emp1.disp_info()

emp2 = Employee()
emp2.get_info()
emp2.disp_info()