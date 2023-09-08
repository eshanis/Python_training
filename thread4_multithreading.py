# NOTE: you can have multiple threads
#creating multiple threads


import time
import threading
start=time.perf_counter()

def do_something():
	print("sleeping for 1 second..")
	time.sleep(1)
	print("Done!!")

#creating the thread object
t1=threading.Thread(target=do_something) # have to specify target or nothing will happen. no error either
t2=threading.Thread(target=do_something)
t1.start()
t2.start()
t1.join()
t2.join() # has the same result even if this is not there

finish=time.perf_counter()
print(f"Finish time: {round(finish-start,1)}second(s)")

print("============= join in different spots ====================")
def do_something():
	print("sleeping for 1 second..")
	time.sleep(1)
	print("Done!!")

#creating the thread object
t1=threading.Thread(target=do_something) # have to specify target or nothing will happen. no error either
t2=threading.Thread(target=do_something)
t1.start()
t1.join()

t2.start()
t2.join() # has the same result even if this is not there

finish=time.perf_counter()
print(f"Finish time: {round(finish-start,1)}second(s)")