#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
This is a bare bone code for linear interpolation
written by Dr. Md. Enamul Hoque, Department of Physics, SUST.
(c) mjonyh@gmail.com 2019

Formulae:
    f(x) = fi + (fi+1 - fi) * (x - xi) / (xi+1 - xi)
'''

# 1. import necessary package, library or module here
import matplotlib.pyplot as plt

def linearinterpolation(xGiven, yGiven, xline, yline):
    stop = xGiven[-1]
    x = xGiven[0]

    fi = yGiven[0]
    fl = yGiven[1]
    xi = xGiven[0]
    xl = xGiven[1]

    while (x <= stop):
        f = fi + (fl - fi) * (x - xi) / (xl - xi)
        xline.append(x)
        yline.append(f)
        x = x + 0.001

    return xline, yline

# 2. define data set (list of x and y) and iteration number
xGiven = [2, 4, 5, 8, 9, 10]
yGiven = [3, 5, 3, 8, 7, 10]
xline = []
yline = []

# 3. user defined function call

for i in range(len(xGiven)-1):
    xlist = [xGiven[i], xGiven[i+1]]
    ylist = [yGiven[i], yGiven[i+1]]
    xline, yline = linearinterpolation(xlist, ylist, xline, yline)

# print(xline, yline)

# 4. plot data point in red and linear fit in green
plt.plot(xGiven, yGiven, 'ro', label='Given data point')
plt.plot(xline, yline, 'g--', label='Linear fit')

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()

plt.show()
