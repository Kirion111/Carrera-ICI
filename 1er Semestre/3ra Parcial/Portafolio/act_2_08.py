from arrayManager import arrayManager as A_Manager
manager = A_Manager()

manager.defineRange(1, 10)

n = 4
mat1 = manager.createMatrix(n, n)
mat2 = manager.createMatrix(n, n)

manager.defineRange(0, 0)
finalMat = manager.createMatrix(n, n)

print("Matrices 1 y 2: \n")
A_Manager.printMatrix(mat1)
A_Manager.printMatrix(mat2)

for i in range(0, len(mat1)):
    for j in range(len(mat1[i])):
        finalMat[i][j] = mat1[i][j] + mat2[i][j]

print("Matriz final: \n")
A_Manager.printMatrix(finalMat)