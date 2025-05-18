import os
import time
import sys

def fork_demo():
    pid = os.fork()
    if pid == 0:
        # print("Child: Exiting (becomes zombie until collected).")
        os._exit(0)
    else:
        # print("Parent: Created child process. Sleeping to let it become zombie.")
        time.sleep(5)
        # print("Parent: Collecting zombie with wait().")
        os.wait()
        # print("Parent: Zombie collected.\n")

def orphan_demo():
    pid = os.fork()
    if pid == 0:
        # print("Child: Waiting after parent exits (becomes orphan).")
        time.sleep(3)
        # print("Child: Parent exited. Now adopted by init/systemd.")
        os._exit(0)
    else:
        # print("Parent: Exiting immediately after creating child (to orphan it).")
        return

def execve_demo():
    pid = os.fork()
    if pid == 0:
        # print("Child: Replacing myself using execve().")
        os.execve("/bin/echo", ["echo", "Hello from execve!"], os.environ)
    else:
        os.wait()
        # print("Parent: execve child finished.\n")

if __name__ == "__main__":
    print("\n--- Zombie Process Demo ---")
    fork_demo()
    time.sleep(1)

    print("\n--- Orphan Process Demo ---")
    orphan_demo()
    time.sleep(5)

    print("\n--- Execve Demo ---")
    execve_demo()



# import os
# import time
# import sys

# def fork_demo():
#     pid = os.fork()
#     if pid == 0:
#         print(f"[Child] PID: {os.getpid()} from Parent PID: {os.getppid()}")
#         print("[Child] Exiting...")
#         os._exit(0)
#     else:
#         print(f"[Parent] PID: {os.getpid()} created Child PID: {pid}")
#         time.sleep(5)  # Let child become zombie
#         print("[Parent] Collecting zombie using wait()")
#         os.wait()
#         print("[Parent] Done.")

# def orphan_demo():
#     pid = os.fork()
#     if pid == 0:
#         print(f"[Orphan Child] PID: {os.getpid()}, Parent PID: {os.getppid()}")
#         time.sleep(3)  # Let parent exit
#         print(f"[Orphan Child] New Parent PID (should be 1 or init/systemd): {os.getppid()}")
#         print("[Orphan Child] Exiting.")
#         os._exit(0)
#     else:
#         print(f"[Parent] PID: {os.getpid()} creating child and exiting.")
#         # Do not use os._exit(0) here, or it will terminate the whole script
#         # Instead, allow the function to return so the rest of the code can run
#         return

# def execve_demo():
#     pid = os.fork()
#     if pid == 0:
#         print(f"[Exec Demo] Before execve() in Child PID: {os.getpid()}")
#         os.execve("/bin/echo", ["echo", "Hello from execve!"], os.environ)
#         # os.execve replaces the process image, so code below won't run
#     else:
#         os.wait()
#         print("[Parent] Finished waiting for execve child.")

# if __name__ == "__main__":
#     print("\n--- Fork and Zombie Demo ---")
#     fork_demo()
#     time.sleep(2)

#     print("\n--- Orphan Process Demo ---")
#     orphan_demo()
#     time.sleep(5)

#     print("\n--- Execve Demo ---")
#     execve_demo()