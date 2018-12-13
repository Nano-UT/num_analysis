import numpy as np
import matplotlib.pyplot as plt
import random

e = 0.00001

print("input the size of matrix:")
n = int(input())
A = np.zeros((n,n))

print("define c:")
c = int(input())

A[0][0] = c
for i in range(1,n):
    A[i][i] = c
    A[i-1][i] = -1
    A[i][i-1] = -1

x = np.empty((n,1))
for i in range(n):
    x[i][0] = random.gauss(0,1)
b = np.empty((n,1))
for i in range(n):
    b[i][0] = random.gauss(0,1)

j = 0

res_error = []

while(True):
    for i in range(n):
        x[i][0] = (- sum(np.dot(A[i],x)) + b[i][0]) / A[i][i] + x[i][0]
    j += 1
    res_error.append(np.linalg.norm(np.dot(A,x)-b))
    if res_error[-1] < e or j >= 100000:
        break

if j == 100000:
    print("Not solved")
else:
    print("steps:",j)
plt.plot(res_error)
plt.title("GS method, size: " + str(n) + ", c = " + str(c))
plt.xlabel("steps")
plt.ylabel("residual error")
plt.show()
