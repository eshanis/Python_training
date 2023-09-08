# calling the same subject multiple times
# starting a thread multiple times
# you cannot start the same thread twice

import time
import threading
start = time.perf_counter()
def do_something():
	print("sleeping for 1 second..")
	time.sleep(1)
	print("Done!!")

# creating the thread object
# how to do same process multiple times / input multiple times/ process multiple times.
# use a loop
# call this thread multiple times. example 10 times

for i in range(10):

	t1 = threading.Thread(target=do_something, name="given 	name Sub-Thread")  # have to specify target or nothing 	will happen. no error either
	t1.start()
	# t1.join()

finish = time.perf_counter()
print(f"\nFinish time: {round(finish - start, 1)}second(s)")