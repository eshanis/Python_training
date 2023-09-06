### __str__()

#used for typecasting
#used for displaying object information

num = 40
res = str(num)
print(res, type(res))

print("++++++++++++++++++++++")
#below is same as above

num = 40
res=int.__str__(num)
print(res, type(res))


print(" ===== in the below , object ID is displayed but we want employee info =========")

class Employee:
	def __init__(self):
		self.name = "Rob"
		self.sam=99999

obj = Employee()
print(obj)

#in the above , object ID is displayed

print("=========== str method used for displaying object information ================")
class Employee:
	def __init__(self):
		self.ename = "Rob"
		self.sal=99999

	def __str__(self):
		return f'Ename= ' + self.ename + ' ' + 'Salary= ' + str(self.sal)
#no print statement here needed. need to "return"

obj = Employee()
print(obj)

#can also be written as below
'''
	def __str__(self):
		print(f'Ename= ' + self.ename + ' ' + 'Salary= ' + str(self.sal))
		return " "
'''

