#declare
#compute function
#a,b initialize
#rows,colb
# thread array
#threading.thread  ,thread array append  , thread.start
# thread.join
# print






import threading

# Global result matrix
result = []

# Thread function: calculates one element of result matrix
def compute_element(A, B, i, j):
    res = 0
    for k in range(len(B)):
        res += A[i][k] * B[k][j]
    result[i][j] = res

# Main program
A = [[1, 2], [3, 4]]     # Matrix A (2x2)
B = [[5, 6], [7, 8]]     # Matrix B (2x2)

# Rows and columns
rows_A = len(A)
cols_B = len(B[0])

# Initialize result matrix with zeros (simplest way)
result = [[0]*cols_B for _ in range(rows_A)]

threads = []

# Create thread for each element in result matrix
for i in range(rows_A):
    for j in range(cols_B):
        t = threading.Thread(target=compute_element, args=(A, B, i, j))
        threads.append(t)
        t.start()  # pthread_create

# Wait for all threads to finish
for t in threads:
    t.join()     # pthread_join

# Display result matrix
print("Resultant Matrix:")
for row in result:
    print(row)
