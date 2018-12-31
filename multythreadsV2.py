#!/usr/bin/env python3
# ----------------------------------------------------------------------------
# Purpose : Simple multithread script to explain the process.
#          Simplified process where queue is filled in advance before processing.
# 		   Processing 20 items with 5 threads each.
# Author:       Denny Vettom
# Dependencies: Python3
#
# Source : https://www.youtube.com/watch?v=NwH0HvMI4EA
# Watch above video for detailed instructions.
# With fix for threads hanging at end of function. 
import threading
from queue import Queue
import time


print_lock = threading.Lock()

def exampleJob():
    while True:
        worker = q.get()
        time.sleep(1)
        with print_lock:
            print(threading.current_thread().name, worker)
        q.task_done()

# Set queue to store values
q = Queue()


# Record Start time
start = time.time()

# Work load, adding some data to queue for the threads to process. 
for worker in range(20):
    q.put(worker)

# Define the number of threads. This section starts number of threads specified and each calls Target function.
for X in range(5):
    t = threading.Thread(target = exampleJob, daemon = True)
    t.start()
# Wait for all the values in queue to be processed.
q.join() 

print ('Job took ', time.time() - start)

# If not returned to prompt, at lease one thread is hung/not finished.