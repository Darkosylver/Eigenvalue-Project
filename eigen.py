import sympy as sym
import matplotlib as plot
import numpy as num

matrixSize = int(input("Enter the matrix size"))
matrix = []

print("Enter each row in the matrix")

for Row in range(matrixSize):
    row = []
    for Column in range(matrixSize):
        row.append(int(input()))
    matrix.append(row)

