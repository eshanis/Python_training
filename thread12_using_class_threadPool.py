# MOST RECENT VERSION FOR MULTITHREADING : THREAD POOL EXECUTION
# added in python 3.2 version
# using concurrent futures

import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
	print(f"sleeping {seconds} second(s)..")
	time.sleep(seconds)
	return "Done sleeping..........!!"


# t1=threading.Thread(target=do_something, name= "given name Sub-Thread")
# t1.start()
# t1.join()

with concurrent.futures.ThreadPoolExecutor() as executor:
	f1 = executor.submit(do_something, 1)  # 1 is the sleep time
	print(f1.result())

finish = time.perf_counter()
print(f"\nFinish time: {round(finish - start, 1)}second(s)")