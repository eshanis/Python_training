#MORE THAN ONE THREAD

import concurrent.futures
import time
start = time.perf_counter()

def do_something(seconds):
	print(f"sleeping {seconds} second(s)..")
	time.sleep(seconds)
	return "Done sleeping..........!!"

with concurrent.futures.ThreadPoolExecutor() as executor:
	f1=executor.submit(do_something,1) # 1 is the sleep time
	f2=executor.submit(do_something,1)
	print(f1.result())
	print(f2.result())

finish = time.perf_counter()
print(f"\nFinish time: {round(finish - start, 1)}second(s)")