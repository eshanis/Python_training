print([x for x in range(10)])

print("==============================")

print([x**2 for x in range(10)])

print("=======INSTEAD OF USING BELOW USE LIST COMPREHENSION AS SHOWN ABOVE=======================")
list = []
for x in range(10):
	list.append(x**2)
print(list)

print("=============== USING LIST COMPREHENSION TO CALL SAME SUBJECT MULTIPLE TIMES ==========================")

# LIST OF THREAD : MULTIPLE SUBMIT: HOW TO CALL SUBJECT MULTIPLE TIMES
# USING COMPREHENSION
# USE COMPREHENSIVE WAY TO CALL SUBJECT MULTIPLE TIMES

import concurrent.futures
import time
start = time.perf_counter()

def do_something(seconds):
	print(f"sleeping {seconds} second(s)..")
	time.sleep(seconds)
	return "Done sleeping..........!!"


with concurrent.futures.ThreadPoolExecutor() as executor:
	# f1=executor.submit(do_something,1) # 1 is the sleep time
	# f2=executor.submit(do_something,1)
	# print(f1.result())
	# print(f2.result())

	#USING COMPREHENSION AS SEEN BELOW
	results=[executor.submit(do_something, 1) for x in range(10)]

finish = time.perf_counter()
print(f"\nFinish time: {round(finish - start, 1)}second(s)")