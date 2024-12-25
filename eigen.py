import numpy as num
import time as time

def powerMethod(matrix, matrixSize, initialValue):
    eigenVector = num.empty((1,matrixSize), float)
    eigenValue = 0
    count = 1
    while not num.array_equal(eigenVector,initialValue):
        if count != 1:
            initialValue = eigenVector
        eigenVector = num.dot(matrix,initialValue)
        eigenValue = num.max(eigenVector)
        eigenVector = num.divide(eigenVector, eigenValue)
        count+=1
    return eigenValue, eigenVector

def powerMethodAnalysis(matrix, matrixSize, initialValue):
    eigenValue, eigenVector = powerMethod(matrix,matrixSize,initialValue)
    matrixDeflated = matrix - eigenValue * num.dot(eigenVector, eigenVector.transpose())    
    eigenValue2nd, eigenVector2nd = powerMethod(matrixDeflated, matrixSize, initialValue)
    convergenceRate = abs(eigenValue/eigenValue2nd)
    return eigenValue, eigenVector, convergenceRate

def QRDecomposition(matrix, matrixSize, max_iterations=1000, tolerance=1e-10):
    eigenVector = num.eye(matrixSize)
    matrixCopy = matrix.copy()
    for _ in range(max_iterations):
        Q, R = num.linalg.qr(matrixCopy)
        matrixCopy = num.dot(R, Q)
        eigenVector = num.dot(eigenVector, Q)
        
        off_diagonal_norm = num.linalg.norm(matrixCopy - num.diag(num.diagonal(matrixCopy)))
        if off_diagonal_norm < tolerance:
            break

    eigenValues = num.diag(matrixCopy)
    return eigenValues, eigenVector

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

startTime = time.time()
eigenValue, eigenVector, convergenceRate = powerMethodAnalysis(matrix,matrixSize,initialValue)
endTime = time.time()

print("Power Method: \n")
print("EigenValue is", eigenValue)
print("Eigen Vector is")
print(eigenVector)
print("Rate of Convergence:", convergenceRate)
print("Computational Time: \n\n", endTime - startTime)

startTime = time.time()
eigenValue, eigenVector = QRDecomposition(matrix,matrixSize)
endTime = time.time()

print("QR Decomposition: \n")
print("EigenValue is", eigenValue)
print("Eigen Vector is")
print(eigenVector)
print("Computational Time: \n\n", endTime - startTime)









