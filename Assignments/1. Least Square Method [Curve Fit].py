#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 02:32:24 2020
@author: S.M. Raihanul Bashir Hridoy
Reg No. 2017132031
"""

# Method Description:
# Here I am taking the data points of x and y as matrices.
# Then, using the numpy stacking function, I am staking those 
# matrices to produce a multi-dimensional matrix. 
# 
# I mutiplied the stacked matrix with its transpose and inverse
# the whole matrix. Then multiplied it with the data points to 
# produce the final matrix whose degree will be responsible for
# plot fitting. 
# 
# Then, I've run a for loop within the range of this degree
# following the equation:
#         y = a * (b**x)
# and plot the points to get the curve

# import various libraries and corresponding packages
import numpy as np
import matplotlib.pyplot as plt


# given data points turned into matrix
m = np.array([[1,5], [4,20], [7,52], [11,121], [15,228], [20,403],[30,903], [50,2504],[77,5929], [92,8464], [100,10005]])

AT = np.ones(m.shape[0]) # new array of given shape
for d in range(1, 10):
    AT = np.vstack((m[:, 0]**d, AT)) # stack the arrays vertically in sequence
A = np.transpose(AT)
ATAinv = np.linalg.inv(np.dot(AT, A)) # computing inverse of matrices
b = m[:, 1]
dot_prod = np.dot(ATAinv, AT)
a = np.dot(dot_prod, b) # taking dot product

degree = a.size - 1
plt.plot(m[:, 0], m[:, 1], 'o')
x = np.linspace(np.amax(m, axis=0)[0],
                np.amin(m, axis=0)[0], 100) # evenly spaced intervals between max and min value
yp = a[degree]
for d in range(degree):
    yp = yp + a[d]*(x**(degree - d))
plt.plot(x, yp)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid()
plt.show()
