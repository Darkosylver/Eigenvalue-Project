import sympy as sym
import matplotlib as plot
import numpy as num

def powerMethod(matrix, matrixSize, initialValue):
    eigenVector = num.empty((1,matrixSize), float)
    eigenValue = 0
    while not num.array_equal(eigenVector,initialValue):
        eigenVector = num.dot(matrix,initialValue)
        eigenValue = num.max(eigenVector)
        eigenVector = num.divide(eigenVector, eigenValue)
        initialValue = eigenVector
    print("Eigen Value is", eigenValue)
    print("Eigen Vector is")
    print(eigenVector)

matrixSize = int(input("Enter the matrix size: "))
matrix = num.empty((matrixSize,matrixSize), int)

print("Enter each entry in a single line, separate numbers by space: ")

entries = list(map(int, input().split()))

matrix = num.array(entries).reshape(matrixSize, matrixSize)

print(matrix)

initialValue = num.empty((1,matrixSize), float)

print("Enter Initial Value, same as the matrix: ")

entries = list(map(float, input().split()))

initialValue = num.array(entries).reshape(matrixSize,1)

print(initialValue)

powerMethod(matrix,matrixSize,initialValue)








