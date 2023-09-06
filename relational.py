#RELATIONAL
"""
__lt__(self,other)  #less than
__gt__(self,other)  #greater than
__le__(self,other)  #less than or equal
__ge__(self,other)  #greater than on equal
__eq__(self,other)  #equal
__ne__(self,other)  #not equal

"""

class Employee:
	def __init__(self,name,exp):
		self.name = name
		self.exp=exp

	def __gt__(self,other): #self= emp1, other = emp2
		return self.exp > other.exp #boolean

	def __lt__(self, other):  # self= emp1, other = emp2
		return self.exp < other.exp  # boolean

emp1=Employee("Jack", 5)
emp2=Employee("Jill", 15)

print("Emp1 Jack is higher experience than Emp2 Jill") if emp1>emp2 else print("Emp2 Jill is higher experience than Emp1 Jack")
print("Emp1 Jack has lesser experience than Emp2 Jill") if emp1<emp2 else print("Emp2 JIll has lesser experience than Emp1 Jack")
#RULES
#if emp1>emp2 # direct comparison os not possible so
#calling object = emp1
#method = __gt__
#argument = emp2



