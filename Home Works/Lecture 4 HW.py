#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 14:17:18 2020

@author: S.M. Raihanul Bashir Hridoy
"""

import matplotlib.pyplot as plt
import math

T = float(input("Enter Time = "))

G = 6.67*10**(-11)

M = 5.97*10**24

R = 6371000

h=[]
t=[]

for i in range(50):

    H = ((G*M*T**2)/4*(math.pi)**2)**(1/3) - R
    h.append(H)
    t.append(T)
    T = T + 100
    
plt.plot(h,t,'ro')
plt.xlabel('x label with unit')
plt.ylabel('y label with unit')

plt.show()
