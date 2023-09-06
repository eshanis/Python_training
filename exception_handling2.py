'''
num1= int(input("enter number: "))
num2= int(input("enter number: "))

try:
	list=[1,2,3,4]
	print(list[4])
	res=num1/num2
	print(res)
except ZeroDivisionError as err:
	print(err)  #ZeroDivisionError : division by zero
        #user defined error message can be f=given too
	print("denominator cannot be zero")

except IndexError as e:
	print(e)

print("+++++++++++++ value error+++++++++++++")

try:
	x=int(input("enter val: "))  # when you enter a string it gives value error
except ValueError as error:
	print(error)

'''

print("+++++++++ generic error message +++++++++++++++++")

try:
	x=int(input("enter val: "))  # if you enter an integer it goes to the list
									#if you enter a string it goes to the except as exception block
	list=[1,2,3,4]
	print(list[4])
	#res=num1/num2
	#print(res)

except IndexError as e:
	print(e)

except Exception as err: #generic
	print(err)

'''	
NOTE:
if placed inbetween no other errors will be handled and will THROW A SYNTAX error. NEEDS TO BE PLACED AT THE END 
except: #generic
	print("Error Occured") 
	
'''
