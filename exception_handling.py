# for list of built in errors
error= dir(locals()['__builtins__'])
print(error)


#IMPLEMENTATION
"""
try:
	#Statement where the error might occur
except:
	# code for handling error and message to be printed when error occurs. this will be executed only if there is an error if not goes to the else block 
else:
	#executed when there is no exception so put message if there is not error like "successful" 
finally:
	#will be irrespective of whetheer exception occured or not
	#what statement to put here? 
	# if there is an interruption close the app
	# even if successful, close the app. 
	# example closing atm whether there is success or failure

"""

num1= int(input("enter number: "))
num2= int(input("enter number: "))

try:
	res=num1/num2
	print(res)
except ZeroDivisionError as err:
	print(err)  #ZeroDivisionError : division by zero
	# user defined error message can be f=given too
	print("denominator cannot be zero")