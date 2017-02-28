# -*- coding:utf-8 -*- 

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x) + 0.5 * x

x = np.linspace(-2 * np.pi, 2 * np.pi, 50)
#reg = np.polyfit(x, f(x), deg = 7)
#reg = np.polyfit(x, f(x), deg = 9)
#ry = np.polyval(reg, x)

matrix = np.zeros((3 + 1, len(x)))

matrix[3, :] = np.sin(x)
#matrix[3, :] = x ** 3
matrix[2, :] = x ** 2
matrix[1, :] = x
matrix[0, :] = 1
#print matrix
print f(x).shape
reg = np.linalg.lstsq(matrix.T, f(x))
print reg[1]
print reg[2]
reg = reg[0]

ry = np.dot(reg, matrix)


#print ry
print reg

print np.allclose(f(x), ry)
print np.sum((f(x) - ry) ** 2) / len(x)


plt.plot(x, f(x), 'b', label = "f(x)")
plt.plot(x, ry, 'r.', label = "regression")
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')




plt.show()
