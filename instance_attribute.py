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

print("+++++++++++++++++++")

class Employee:

	def eID_Gen(self):
		self.empid = 100
		self.empid+=1

	def disp_Id(self):
		print("Employee id: ", self.empid)

emp1 = Employee()
emp1.eID_Gen()
emp1.disp_Id()

emp2 = Employee()
emp2.eID_Gen()
emp2.disp_Id()

emp3 = Employee()
emp3.eID_Gen()
emp3.disp_Id()