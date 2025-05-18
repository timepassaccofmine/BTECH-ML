import threading
import time
import random

# Buffer and size
buffer = []
BUFFER_SIZE = 5

# Semaphores
empty = threading.Semaphore(BUFFER_SIZE)  # initially all slots are empty
full = threading.Semaphore(0)             # initially no item is produced

# Mutex lock
mutex = threading.Lock()    #☝️ Lock

# Producer function
def producer():
    for i in range(10):  # produce 10 items
        item = random.randint(1, 100)
        empty.acquire()          # wait if buffer is full
        mutex.acquire()          # enter critical section

        buffer.append(item)
        print(f"Producer produced: {item}")

        mutex.release()          # exit critical section
        full.release()           # signal that an item was added
        time.sleep(random.random())  # simulate delay

# Consumer function
def consumer():
    for i in range(10):  # consume 10 items
        full.acquire()           # wait if buffer is empty
        mutex.acquire()          # enter critical section

        item = buffer.pop(0)
        print(f"Consumer consumed: {item}")

        mutex.release()          # exit critical section
        empty.release()          # signal that an item was removed
        time.sleep(random.random())  # simulate delay

# Main program
if __name__ == "__main__":
    # Create producer and consumer threads
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Finished producing and consuming.")
