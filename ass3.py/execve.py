import os
import sys
import time

def execute_with_execve():
    path = "C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Python\\Python311\\python.exe"
    argv = [path, "second.py"]
    envp = os.environ
    try:
        os.execve(path, argv, envp)
    except OSError as e:
        print(f"Error executing command: {e}")
        sys.exit(1)

file_name = os.path.basename(__file__)
print(f"PID: {os.getpid()} | MSG: Hello, this is inital process ({file_name}).")
execute_with_execve()

print("This line will never be executed!")
