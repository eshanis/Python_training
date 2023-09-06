print("MRO Exception ", Exception.mro())
print("MRO Exception ", IndexError.mro())
print("MRO Exception ", ValueError.mro())

#CUSTOM EXCEPTION

#==> inherit from exception class (built in class)
"""
class customError(exception):
	pass

try:
	code to handle
except customError:
	error message to be printed
"""
print("+++++++++++++ custom error +++++++++++++++++++++")
class customError(Exception):
	pass

try:
	print("I am try block ...!!")
	raise customError("This is my custom exception")

except customError as e:
	print(e)

print("+++++++++++++ ELIGIBLE TO VOTE CHECK +++++++++++++++++++++")
"""
18 to 70 => no exception => "eligible to vote"
<18      => too young => "you are too young to vote"
>70      =>  too old  => "too old, not eligible"

"""
class tooOld(Exception):
	def __init__(self,arg):
		self.msg=arg

class tooYoung(Exception):
	def __init__(self,arg):
		self.msg=arg

try:
	age=int(input("enter age: "))
	if age>70:
		raise tooOld("too old, not eligible")
	elif age <18:
		raise tooYoung("you are too young to vote")
	else:
		print("eligible to vote")

except tooOld as err:
	print(err)

except tooYoung as err:
	print(err)

print("++++++++++++++ alternate way using str ++++++++++++")

class tooOld(Exception):
	def __str__(self):
		return "Too Old"

class tooYoung(Exception):
	def __str__(self):
		return "Too Young"

try:
	age=int(input("enter age: "))
	if age>70:
		raise tooOld("too old, not eligible")
	elif age <18:
		raise tooYoung("you are too young to vote")
	else:
		print("eligible to vote")


except tooOld as err:
	print(err)

except tooYoung as err:
	print(err)


