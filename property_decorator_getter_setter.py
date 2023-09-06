#PROPERTY DECORATOR
# setter ==> accepting value and update the private attribute
#         ==> also called mutator

"""
getter ==> which is used to retrn value
        ==> no parameter
        ==>should return the private attribute only then we can access
 	==> accessor method
"""

class Customer:
	def __init__(self,id,name,age,wallet_balance):
		self.id = id
		self.name=name
		self.age = age
		self.__wallet_balance=wallet_balance #this is private attribute

cust1=Customer(110, "Sam", 20, 99999)
print(cust1.age)
cust1.age = 22
print(cust1.age) # this is updated since it is public wallet is private and cannot be changed outside

print("+++++++++++  setters and getters +++++++++++++++++++++++")


class Customer:
	def __init__(self, id, name, age, wallet_balance):
		self. id = id
		self.name = name
		self.age = age
		self.__wallet_balance = wallet_balance  # this is private attribute

	def set_walletBalance(self, amt):  # setter
		self.__wallet_balance = amt

	def get_walletBalance(self):  # getter
		return self.__wallet_balance


cust1 = Customer(110, "Sam", 20, 99999)
print(cust1.age)
cust1.age = 22
print(cust1.age)  # this is updated since it is public wallet is private and cannot be changed outside
cust1.set_walletBalance(99999)  # access private attributes using public methods
print(cust1.get_walletBalance())