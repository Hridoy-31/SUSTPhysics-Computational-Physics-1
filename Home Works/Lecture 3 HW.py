#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 21:29:18 2020

@author: S.M. Raihanul Bashir Hridoy
"""

import math

T = float(input("Enter Time = "))

G = 6.67*10**(-11)

M = 5.97*10**24

R = 6371000

for i in range(10):

    H = ((G*M*T**2)/(4*math.pi**2))**(1/3) - R
    
    if (H<0):
        print(f"\nHeight is still negative at {T} sec")
        
    else:
        print(f"\nThe height is = {H} at {T} sec")
        
    T = T + 1000
