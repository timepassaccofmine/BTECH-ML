import os
import sys
import time

def create_zombie():
    pid = os.fork()

    if pid == 0:
        print(f"PID {os.getpid()} | Child is Running....")
        print(f"PID {os.getpid()} | Child is Exiting....")
    else:
        print(f"PID {os.getpid()} | Parent is Running....")
        time.sleep(60)
        print(f"PID {os.getpid()} | Parent is Exiting....")
        sys.exit(0)


create_zombie()
