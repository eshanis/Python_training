# LIST OF THREAD to access the threads and manage them

import time
import threading
start = time.perf_counter()

def do_something():
	print("sleeping for 1 second..")
	time.sleep(1)
	print("Done!!")


# LIST OF THREAD

# use a loop
# call this thread multiple times. example 10 times
threads_var = []
for i in range(10):

	t1 = threading.Thread(target=do_something,name="given 	name Sub-Thread")  # have to specify target or nothing 	will happen. no error either
	t1.start()
	# t1.join()
	threads_var.append(t1)

for thread in threads_var:
	thread.join()

finish = time.perf_counter()
print(f"\nFinish time: {round(finish - start, 1)}second(s)")