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


"""
Simplified version where thread calls the function direct and examplejob gets data from queue and process it.
There is a worker loop to add 20 values to queue q for the threads to consume.
Threaders starts 5 threads and each calling example job.
Examplejob reads data from the queue and process it.
q.join ensure all data in queue is processed befoe exit.
"""

# Defining print lock so that each thread can do complete print than mix up data.
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
for worker in range(27):
    q.put(worker)

# Define the number of threads. This section starts number of threads specified and each calls Target function.
for X in range(5):
    t = threading.Thread(target = exampleJob, daemon = True)
    t.start()
# Wait for all the values in queue to be processed.
q.join() 

print ('Job took ', time.time() - start)

# If not returned to prompt, at lease one thread is hung/not finished.