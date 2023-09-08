print("+++++++++++++++++++  Naming the thread +++++++++++++++++")
# NAMING A THREAD

import time
import threading
start=time.perf_counter()
def do_something():
	print("sleeping for 1 second..")
	time.sleep(1)
	print("Done!!")
	print("\nThread Name: ", threading.current_thread().name)

#creating the thread object
t1=threading.Thread(target=do_something, name= "given name Sub-Thread"  ) # have to specify target or nothing will happen. no error either

t1.start()


print("\nThread Name after start: ", threading.current_thread().name)
finish=time.perf_counter()
print(f"\nFinish time: {round(finish-start,1)}second(s)")