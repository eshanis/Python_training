
num1 = int(input("enter number: "))
num2 = int(input("enter number: "))

try:

	res = num1 / num2

except ZeroDivisionError as err:
	print(err)  # ZeroDivisionError : division by zero
	# user defined error message can be f=given too
	print("denominator cannot be zero")

else:
	print(res) # will print result only if not divided by zero
finally:
	print("end of program")  # will be executed everytime
