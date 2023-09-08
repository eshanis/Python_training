print("============ using thread and join ==============")
# no synchronization above.
# but if output of one thread is input of another, then we NEED SYNCHRONIZATION
# for this use Thread with join. this will have the main thread to wait and
#until process in complete then move to sub thread
# NOTE: you cannot start the same thread twice 

# to do above using threading and join

import time
import threading
start=time.perf_counter()

def do_something():
	print("sleeping for 1 second..")
	time.sleep(1)
	print("Done!!")

#creating the thread object
t1=threading.Thread(target=do_something) # have to specify target or nothing will happen. no error either
t1.start()
#t1.start() # gives error  # NOTE: you cannot start the same thread twice
t1.join()

finish=time.perf_counter()
print(f"Finish time: {round(finish-start,1)}second(s)") # process completed in 1 second