#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 18:48:36 2020
A Big Thanks goes to Mamunur Rashid for helping me in theory !!!!
@author: S.M. Raihanul Bashir Hridoy
"""

import matplotlib.pyplot as plt
import numpy as np

def Lagrange_Interpolation(x, xi, fi):
  result = 0

  for i in range(len(xi)):
    p = fi[i]

    for j in range(len(xi)):
      if (i != j):
        p = p * ((x - xi[j]) / (xi[i] - xi[j]))
      
    result = result + p;

  return result

x = [2, 4, 7, 10, 15, 17, 22, 25, 30]
y = [4, 5, 3, 7, 9, 5, 14, 18, 15]

plt.plot(x, y, 'o', label = 'Data Points')
x_plot = np.arange(x[0], x[-1], 0.001)
plt.plot(x_plot, Lagrange_Interpolation(x_plot, x, y), '--', label = 'Interpolated Data')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.show()
