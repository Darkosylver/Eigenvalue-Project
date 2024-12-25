import numpy as num
import time as time

def powerMethod(matrix, matrixSize, initialValue, max_iterations=1000, tolerance=1e-10):
    eigenVector = num.empty((1,matrixSize), float)
    eigenValue = 0
    count = 1
    while not num.array_equal(eigenVector,initialValue) or count <= max_iterations:
        if count != 1:
            initialValue = eigenVector
        eigenVector = num.dot(matrix,initialValue)
        eigenValue = num.max(eigenVector)
        eigenVector = num.divide(eigenVector, eigenValue)
        count+=1
        if (num.linalg.norm(eigenVector - initialValue) < tolerance):
            break
    return eigenValue, eigenVector

def powerMethodAnalysis(matrix, matrixSize, initialValue):
    eigenValue, eigenVector = powerMethod(matrix,matrixSize,initialValue)
    matrixDeflated = matrix - eigenValue * num.dot(eigenVector, eigenVector.transpose())    
    eigenValue2nd, eigenVector2nd = powerMethod(matrixDeflated, matrixSize, initialValue)
    print("Second largets: ", eigenValue2nd)
    convergenceRate = abs(eigenValue/eigenValue2nd)
    return eigenValue, eigenVector, convergenceRate

def  QRDecomposition(A, size, max_iterations=1000, tolerance=1e-10):
    Ak = A.copy()
    Q_total = num.eye(size)

    for _ in range(max_iterations):
        Q, R = num.linalg.qr(Ak)
        Ak = num.dot(R, Q)
        Q_total = num.dot(Q_total, Q)
        
        off_diagonal_norm = num.linalg.norm(Ak - num.diag(num.diagonal(Ak)))
        if off_diagonal_norm < tolerance:
            break

    eigenvalues = num.diag(Ak)
    
    count = 0
    convergenceRate = num.empty((1, size-1), float)
    while count < 4:
        convergenceRate[0][count] = abs(eigenvalues[count+1]/eigenvalues[count])
        count+=1
    eigenvectors = Q_total
    return eigenvalues, eigenvectors, convergenceRate

matrixSize = int(input("Enter the matrix size: "))
matrix = num.empty((matrixSize,matrixSize), float)

print("Enter each entry in a single line, separate numbers by space: ")

entries = list(map(float, input().split()))

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
print("Computational Time: ", endTime - startTime)
print("\n\n")

startTime = time.time()
eigenValue, eigenVector, convergenceRate = QRDecomposition(matrix,matrixSize)
endTime = time.time()

print("QR Decomposition: \n")
print("EigenValue is", eigenValue)
print("Eigen Vector is")
print(eigenVector)
print("Rate of Convergence:", convergenceRate)
print("Computational Time: ", endTime - startTime)
print("\n\n")









