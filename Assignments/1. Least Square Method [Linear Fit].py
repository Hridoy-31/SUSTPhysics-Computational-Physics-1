#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 08:52:24 2020
@author: S.M. Raihanul Bashir Hridoy
"""

# importing necessary libraries
import matplotlib.pyplot as plt

# taking data points
X = [1, 4, 7, 11, 15, 20, 30, 50, 77, 92, 100]
Y = [5, 20, 52, 121, 228, 403, 903, 2504, 5929, 8464, 10005]

# taking mean of X and Y
avg_x = sum(X) // len(X) #taking the integer division 
avg_x = float(avg_x)

avg_y = sum(Y) // len(Y) #taking the integer division
avg_y = float(avg_y) 

# measuring scatteredness in data points
x_scatter = [x - avg_x for x in X] # using list comprehension
y_scatter = [y - avg_y for y in Y] #using list comprehension

# measuring squared value of scatteredness in data points
x_scatter_squared = [x**2 for x in x_scatter] # using list comprehension
y_scatter_squared = [y**2 for y in y_scatter] # using list comprehension

# using map and lambda for quick function generate & assign functional value
xy = map((lambda x,y:x*y), x_scatter, y_scatter)

# data preparation for plotting
# y = a0 + a1*x
# avg_y = a0 + a1*(avg_x)
a1 = float(sum(xy)) / float(sum(x_scatter_squared))
a0 = avg_y - (a1 * avg_x)

#plotting
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.plot(X,Y,'.')
plt.plot([0,110], [0*a1+a0, 110*a1+a0]) # given range for the straight line
plt.grid() # for grid showing
plt.show()
