#!/usr/bin/env python
# -*- coding: utf-8 -*-

H = float(input('Input Height (in m): '))
T = float(input('Time (in sec): '))

S = 0.5 * 9.81 * T**2

if(H - S > 0):
    print('The height h, is ', H - S, 'm')
else:
    print('The provided time is large!')
