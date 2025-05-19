import os

def child_process():
    parent_pid = os.getppid()
    child_pid = os.getpid()
    print(f"This is the child process.\nParent PID => {parent_pid} \nChild PID => {child_pid}\n")

def parent_process(child_pid):
    parent_pid = os.getppid()
    child_pid = os.getpid()
    print(f"This is the parent process.\nParent PID => {parent_pid} \nChild PID => {child_pid}\n")

pid = os.fork()

if pid == 0:
    child_process()
else:
    parent_process(pid)
