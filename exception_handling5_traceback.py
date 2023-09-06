import traceback

num1= int(input("enter number: "))
num2= int(input("enter number: "))

try:
	x=int(input("enter val: "))
	list=[1,2,3,4]
	print(list[3])
	res=num1/num2
	print(res)

except ZeroDivisionError as err:
	print(err)  #ZeroDivisionError : division by zero
        #user defined error message can be f=given too
	print("denominator cannot be zero")
	traceback.print_exc()

except IndexError as e:
	print(e)
	traceback.print_exc()

except: #generic
	print("Error Occured")
	traceback.print_exc()