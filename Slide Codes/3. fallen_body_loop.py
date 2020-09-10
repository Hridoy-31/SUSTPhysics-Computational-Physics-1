#!/usr/bin/env python
# -*- coding: utf-8 -*-

H = float(input('Input Height (in m): '))

for T in range(10):
    S = 0.5 * 9.81 * T**2
    print('The height h, is ', H - S, 'm at t: ', T)
