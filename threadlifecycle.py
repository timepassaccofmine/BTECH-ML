import threading
import time

# Define a simple function for thread
def thread_task():
    print("Thread is starting...")
    time.sleep(2)  # Simulate thread doing some work
    print("Thread has finished.")
    

# Main program
print("Main thread: Creating a thread")
t = threading.Thread(target=thread_task)

print("Main thread: Starting the thread")
t.start()  # start() moves thread to Runnable state

print("Main thread: Waiting for the thread to finish")
t.join()   # join() waits until thread_task finishes

print("Main thread: Thread has completed")
