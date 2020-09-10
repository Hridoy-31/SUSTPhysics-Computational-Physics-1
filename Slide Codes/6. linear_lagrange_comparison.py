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

def linear_interpolation(xGiven, yGiven, xline, yline):
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

def lagrange_poly(point, x, f):
	'''This is the main function where Lagrange interpolation
	is implemented. This function return the value of f(x)
	corresponds to the x within the domain.'''
	result = 0

	'Loop over j for summation'
	for j in range(len(x)):
		p = 1

		'Loop over k for product'
		for k in range(len(x)):

			'Checking the condition for k and j'
			if k != j:
				p *= float(point - x[k])/float(x[j] - x[k])
		result += p * f[j]

	return result

def lagrange_interpolation(x,y):
	'This function generate new Dataset for Lagrange interpolation'
	initial = x[0]
	dx = float(x[1]-x[0])/10
	n_x = []
	n_y = []

	while initial < x[len(x)-1]+1:
		n_x.append(initial)
		n_y.append(lagrange_poly(initial, x, y))
		initial += dx

	return n_x, n_y

# 2. define data set (list of x and y) and iteration number
xGiven = [2, 4, 5, 8, 9, 10]
yGiven = [3, 5, 3, 8, 7, 10]
xline = []
yline = []

# 3. user defined function call

for i in range(len(xGiven)-1):
    xlist = [xGiven[i], xGiven[i+1]]
    ylist = [yGiven[i], yGiven[i+1]]
    xline, yline = linear_interpolation(xlist, ylist, xline, yline)

# print(xline, yline)

# 4. plot data point in red and linear fit in green
plt.plot(xGiven, yGiven, 'ro', label='Given data point')
plt.plot(xline, yline, 'g--', label='Linear Interpolation')

xline, yline = lagrange_interpolation(xGiven, yGiven)
plt.plot(xline, yline, 'b--', label='Lagrange Interpolation')

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.xlim(xGiven[0], xGiven[-1])
plt.ylim(yGiven[0], yGiven[-1])
plt.legend()

plt.show()
