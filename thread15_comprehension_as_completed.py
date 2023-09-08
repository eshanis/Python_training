#MORE THAN ONE THREAD and AS_COMPLETED()
#as_completed()

import concurrent.futures
import time
start = time.perf_counter()

def do_something(seconds):
	print(f"sleeping {seconds} second(s)..")
	time.sleep(seconds)
	return "Done sleeping..........!!"

with concurrent.futures.ThreadPoolExecutor() as executor:
	results=[executor.submit(do_something,1) for x in range(10)]

	#as_completed(list of thread) is feature of concurrent future
	for f in concurrent.futures.as_completed(results):
		print(f.result())  # this is inbuilt method not the variable

finish = time.perf_counter()
print(f"\nFinish time: {round(finish - start, 1)}second(s)")