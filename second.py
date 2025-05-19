import os
print("hello")
file_name = os.path.basename(__file__)
print(f"PID: {os.getpid()} | MSG: Hello, this is another process ({file_name}).")