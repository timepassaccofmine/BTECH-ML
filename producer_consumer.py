import threading
import time

# Shared Memory variables
CAPACITY = 10
# buffer = [-1 for i in range(CAPACITY)]
buffer = [-1] * CAPACITY
in_index = 0
out_index = 0

print(buffer)
# Declaring Semaphores
mutex = threading.Semaphore()
empty = threading.Semaphore(CAPACITY)
full = threading.Semaphore(0)


# Producer Thread Class
class Producer(threading.Thread):
    def run(self):
        global CAPACITY, buffer, in_index, out_index
        global mutex, empty, full

        items_produced = 0
        counter = 0

        while items_produced < 15:
            empty.acquire()
            mutex.acquire()

            counter += 1
            buffer[in_index] = counter
            in_index = (in_index + 1) % CAPACITY
            print("Producer produced : ", counter)

            mutex.release()
            full.release()

            time.sleep(1)

            items_produced += 1


# Consumer Thread Class
class Consumer(threading.Thread):
    def run(self):
        global CAPACITY, buffer, in_index, out_index, counter
        global mutex, empty, full

        items_consumed = 0

        while items_consumed < 15:
            full.acquire()
            mutex.acquire()

            item = buffer[out_index]
            # "wrap around"  it wraps back around to 0
            out_index = (out_index + 1) % CAPACITY
            print("Consumer consumed item : ", item)

            mutex.release()
            empty.release()

            time.sleep(2.5)

            items_consumed += 1


# Creating Threads
producer = Producer()
consumer = Consumer()

# Starting Threads
consumer.start()
producer.start()

# Waiting for threads to complete
producer.join()
consumer.join()
