# by default one thread is created.  called (main-thread)
# the below is happening in sequential way
# only one main thread
# two ways : cpu bound and input/output bound (reading from file system, downloading from online)

import time
start=time.perf_counter() #performance counter

def do_something():
	print("sleeping for 1 second..")
	time.sleep(1)
	print("Done!!")

do_something() # for one function call it takes 1 second
do_something() # for second call another second so total 2 seconds

finish=time.perf_counter()
print(f"Finish time: {round(finish-start,1)}second(s)")

# to the above using threading

print("=============== using threading same method as above =================")
import time
import threading
start=time.perf_counter()  #performance counter

def do_something():
	print("sleeping for 1 second..")
	time.sleep(1)
	print("Done!!")

#creating the thread object
t1=threading.Thread(target=do_something) # have to specify target or nothing will happen. no error either
t1.start()

finish=time.perf_counter()
print(f"Finish time: {round(finish-start,1)}second(s)")  # process completed in 0.0 seconds


