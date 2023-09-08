#OPTION 1
#import threading  # not needed for inherit from class
#class DerivedThread(threading):
import threading
# implentation using class: THREAD WITH CLASSES
 # INHERIT FROM THREAD CLASS

#OPTION 2

import time
class DerivedThread(threading.Thread):
	def run(self):  # inbuilt function defined in threading module
		time.sleep(2)
		print("\nsub Thread Name after start: ", threading.current_thread().name)

obj = DerivedThread()
obj.start()
obj.join()

print("\nThread Name after start: ", threading.current_thread().name)
