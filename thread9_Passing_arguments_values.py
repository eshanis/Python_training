# PASSING ARGUMENTS / VALUES


# LIST OF THREAD to access the threads and manage them

import time
import threading
start = time.perf_counter()

def do_something(seconds):
	print(f"sleeping {seconds} second(s)..")
	time.sleep(seconds)
	print("Done!!")


# LIST OF THREAD

# use a loop
# call this thread multiple times. example 10 times
threads_var = []
for i in range(10):

	t1 = threading.Thread(target=do_something,args=[1.5])
	t1.start()
	threads_var.append(t1)

for thread in threads_var:
	thread.join()

finish = time.perf_counter()
print(f"\nFinish time: {round(finish - start, 1)}second(s)")