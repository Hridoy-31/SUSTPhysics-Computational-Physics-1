#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 01:04:22 2020
title : Assignment 4 - Faddeev Leverrier method in Python
@author: S. M. Raihanul Bashir
reg no : 2017132031
"""

import numpy as np

def faddeev_leverrier(A):
    '''
    Given an 3 x 3 matrix A, we return the coefficients of it's
    characteristic polynomial
    P(x) ^= det(xI - A) = a0 * x^3 + a1 * x^2 + ... + an
    
    The fundamental property of P(x) that a0 = 1, an = det(A)
    We return the list a = [a0, a1, ..., an]
    '''
    A = np.array(A) #Ensure we have a numpy array
    n = A.shape[0]
    assert A.shape[1] == n, 'Array must be square!'
    cp = []

    a = np.array([1.])
    Ak = np.array(A)
    for k in range(1, n + 1):
        ak = -Ak.trace() / k
        a = np.append(a, ak)
        Ak = np.add(Ak, np.diag(np.repeat(ak, n)), out=Ak, casting="unsafe")
        Ak = np.dot(A, Ak)
        cp.append(a)
    return cp[-1]

def inv_mat(A):
    '''
    Given an 3 x 3 matrix A, we have to find the coefficients of it's
    characteristic polynomial to find out the inverse matrix
    P(x) ^= det(xI - A) = a0 * x^3 + a1 * x^2 + ... + an
    and then for inverse matrix:
    A_inv = (1/a3)*(B2-a2I)
    '''
    A = np.array(A) #Ensure we have a numpy array
    n = A.shape[0]
    assert A.shape[1] == n, 'Array must be square!'

    a = np.array([1.])
    Ak = np.array(A)
    for k in range(1, n + 1):
        ak = -Ak.trace() / k
        a = np.append(a, ak)
        Ak = np.add(Ak, np.diag(np.repeat(ak, n)), out=Ak, casting="unsafe")
        Ak = np.dot(A, Ak)
        if k==1:
            return Ak # returning the B2 matrix to the call position
        


if __name__ == '__main__':
    a = []
    coeff_poly = []
    
    # taking input of the elements of the matrix
    
    print("Enter the elements of a 3x3 matrix : ")
    for i in range(3):
        x = []
        for j in range(3):
            x.append(float(input()))
        a.append(x)
        
    A = np.array(a)
    coeff_poly = faddeev_leverrier(A)

    # finding the characteristic polynomial
    
    print("\nThe characteristic polynomial is the following : ")
    print("\n")
    print(f"P(x) = {coeff_poly[0]}x^3 + {coeff_poly[1]}x^2 + {coeff_poly[2]}x + {coeff_poly[3]}")
    print("\n")
    
    # Finding the inverse matrix
    
    I = np.identity(3) # creating a 3x3 identity matrix
    p2I = (-1)*coeff_poly[2]*I
    B2 = inv_mat(A)
    
    print("The inverse matrix is : \n")
    A_inv = (-1/coeff_poly[3])*np.subtract(B2, p2I) # A_inv = (1/a3)*(B2-a2I)
    np.set_printoptions(precision=2) # set precision upto 2 decimal places
    print(A_inv)
    
    
