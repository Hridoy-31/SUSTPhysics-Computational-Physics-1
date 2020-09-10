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

for i in range(100):

    H = ((G*M*T**2)/(4*math.pi**2))**(1/3) - R
    h.append(H)
    t.append(T)
    T = T + 500
    
plt.plot(t,h,'.')
plt.xlabel('time label with seconds')
plt.ylabel('height label with meters')

plt.show()
