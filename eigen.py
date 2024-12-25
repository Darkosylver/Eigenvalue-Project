import sympy as sym
import matplotlib as plot
import numpy as num

def powerMethod(matrix, matrixSize, initialValue, iterations):
    eigenVector = num.empty((1,matrixSize), float)
    eigenValue = 0
    iterationEigenValue = 0
    iterationEigenVector = num.empty((1,matrixSize), float)
    count = 1
    while not num.array_equal(eigenVector,initialValue):
        if count != 1:
            initialValue = eigenVector
        eigenVector = num.dot(matrix,initialValue)
        eigenValue = num.max(eigenVector)
        eigenVector = num.divide(eigenVector, eigenValue)
        if count == iterations:
            iterationEigenValue = eigenValue
            iterationEigenVector = eigenVector
        count+=1
    if iterations != 0:
        print("EigenValue is", iterationEigenValue)
        print("Real Value is", eigenValue)
        print("Eigen Vector is")
        print(iterationEigenVector)
        print("Real EigenVector is")
        print(eigenVector)
    else:
        print("EigenValue is", eigenValue)
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

iterations = int(input("Enter number of Iterations(for real value, enter 0): "))

powerMethod(matrix,matrixSize,initialValue, iterations)








