#THREADING

#1. Thread is a light weight process.
#2. Each process is divided into multiple processes called thread

#MULTITASKING
#1. mulitple tasks at the same time and one task is not interrupted by another
#2. done by using multicore cpu's

#how to create this thread and how to do manipulation on a thread

#import a threading module
#active_count()  ==>to find total number of active instances
#ennumerate() ==> displays all the active threads

import threading
print("active instances: ", threading.active_count())
print("active threads: ", threading.enumerate())
print(threading.current_thread())