#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 01:25:39 2020
title: Assignment 3 - Matrix summation, subtraction and multiplication 
@author: S. M. Raihanul Bashir
reg no: 2017132031
"""

def zeros_matrix(rows, cols):
    """
    Creates a matrix filled with zeros.
        :param rows: the number of rows the matrix should have
        :param cols: the number of columns the matrix should have
 
        :return: list of lists that form the matrix
    """
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)
 
    return M

def matrix_addition(A, B):
    """
    Adds two matrices and returns the sum
        :param A: The first matrix
        :param B: The second matrix
 
        :return: Matrix sum
    """
    # Ensuring dimensions are valid for matrix addition
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if rowsA != rowsB or colsA != colsB:
        raise ArithmeticError('Matrices are NOT the same size.')
 
    # Creating a new matrix for the matrix sum
    C = zeros_matrix(rowsA, colsB)
 
    # Performing element by element sum
    for i in range(rowsA):
        for j in range(colsB):
            C[i][j] = A[i][j] + B[i][j]
 
    for i in range(rowsA): 
      for j in range(colsB): 
        print(round(C[i][j], 2), end = " ") 
      print()
 
def matrix_subtraction(A, B):
    """
    Subtracts matrix B from matrix A and returns difference
        :param A: The first matrix
        :param B: The second matrix
 
        :return: Matrix difference
    """
    # Ensuring dimensions are valid for matrix subtraction
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if rowsA != rowsB or colsA != colsB:
        raise ArithmeticError('Matrices are NOT the same size.')
 
    # Creating a new matrix for the matrix difference
    C = zeros_matrix(rowsA, colsB)
 
    # Performing element by element subtraction
    for i in range(rowsA):
        for j in range(colsB):
            C[i][j] = A[i][j] - B[i][j]
 
    for i in range(rowsA): 
      for j in range(colsB): 
        print(round(C[i][j], 2), end = " ") 
      print()

def matrix_multiply(A, B):
    """
    Returns the product of the matrix A * B
        :param A: The first matrix - ORDER MATTERS!
        :param B: The second matrix
 
        :return: The product of the two matrices
    """
    # Ensuring A & B dimensions are correct for multiplication
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if colsA != rowsB:
        raise ArithmeticError(
            'Number of A columns must equal number of B rows.')
 
    # Storing matrix multiplication in a new matrix
    C = zeros_matrix(rowsA, colsB)
    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total
 
    for i in range(rowsA): 
      for j in range(colsB): 
        print(round(C[i][j], 2), end = " ") 
      print()


if __name__ == "__main__":
  a = []
  b = []

  row = int(input("Number of rows and columns : "))
  col = row

  print("Enter the elements of first matrix : ")
  for i in range(row):
    x = []
    for j in range(col):
      x.append(float(input()))
    a.append(x)

  print("Enter the elements of second matrix : ")
  for i in range(row):
    x = []
    for j in range(col):
      x.append(float(input()))
    b.append(x)

print("\n")
print("Matrix Summation: \n")
matrix_addition(a,b)
print("\n")
print("Matrix Subtraction: \n")
matrix_subtraction(a,b)
print("\n")
print("Matrix Multiplication: \n")
matrix_multiply(a,b)
print("\n")
