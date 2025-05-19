import os
import sys
import time

def create_orphan():
    pid = os.fork()

    if pid == 0:
        print(f"PID {os.getpid()} | Child is Running....")
        
        for i in range(4):
            print(f"Parent of this process {os.getpid()} is => {os.getppid()}")
            time.sleep(2)

        print(f"PID {os.getpid()} | Child is Exiting....")
    else:
        #parent process
        print(f"PID {os.getpid()} | Parent is Running....")
        print(f"PID {os.getpid()} | Parent is Exiting....")
        sys.exit(0)


create_orphan()
