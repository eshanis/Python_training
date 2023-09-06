print("========== GLOBAL ATTRIBUTES ===========")
# declared outside the class
# can be accessed everywhere

var = "Emp Info"
count = 10

class Employee:

	def get_info(self):  #non static method
		var = "All ok"
		print("message in get_info: ", var)
		print("Disp-get: ", globals()['var']) # calls the global attribute

	def disp_info(self):
		print("message in disp_info: ", var)
		print("Disp: ", globals()['var'])
		print("Disp: ", globals()['count'])

emp1=Employee()
emp1.get_info()
emp1.disp_info()

print("++++++++++++++++ to alter global attribute do below ++++++++++++")
class Employee:

	def get_info(self):  #non static method
		global var
		var = "see the change"
		#var = "All ok"
		print("message in get_info: ", var)
		print("Disp-get: ", globals()['var'])

	def disp_info(self):
		print("message in disp_info: ", var)
		print("Disp: ", globals()['var'])
		print("Disp: ", globals()['count'])

emp1=Employee()
emp1.get_info()
emp1.disp_info()

print("++++++++++++++++ to alter global attribute but use forget to remove local? ++++++++++++")

class Employee:

	def get_info(self):  #non static method
		global var
		var = "see the change"
		var = "All ok"
		print("message in get_info: ", var)
		print("Disp-get: ", globals()['var'])

	def disp_info(self):
		print("message in disp_info: ", var)
		print("Disp: ", globals()['var'])
		print("Disp: ", globals()['count'])

emp1=Employee()
emp1.get_info()
emp1.disp_info()