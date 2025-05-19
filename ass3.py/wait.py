import os
import sys
import time

def demo_wait():
    pid = os.fork()

    if pid == 0:
        print(f"PID {os.getpid()} | Child is Running....")
        for i in range(4):
            print(f"\tChild is Sleeping...({i+1} sec)")
            time.sleep(1)
        print(f"PID {os.getpid()} | Child is Exiting....")
    else:
        os.wait()
        print(f"PID {os.getpid()} | Parent is Running....")
        print(f"PID {os.getpid()} | Parent is Exiting....")


demo_wait()