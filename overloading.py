#OVERLOADING

#1. more than one function has the same name but difference in its function signature/parameter.

#2. for predefined function you can implement it even though you cannot write a function for overloading in Python
#eg add function below
#example

#length of string, list, tuple, dictionary
print(len("Python"))
print(len([1,2,3,4,5]))

print("+++++++++++++++++++++++")

#below will throw an error
#1 the first function is overwrtitten by the second so when
# you call them both error says: add() takes two positional #arguments but three were given
'''
def add(n1,n2,n3):
	return n1+n2+n3

def add(n1,n2):
	return n1+n2

print(add(1,2,3))
print(add(1,2))
'''
print("==== overloading user defined function using default value/argument =========")
#OVERLOADING USER-DEFINED FUNCTION ==>USING  DEFAULT ARGUMENT

def add(n1,n2,n3=0):  # N=0 IS DEFAULT ARGUMENT this will work
	return n1+n2+n3

print(add(10,20,30))
print(add(10,20))