from arrayManager import arrayManager as A_Manager
manager = A_Manager()

manager.defineRange(0, 1)

def checkMat(mat):
    isNotIdenty = False
    for i in range(0, len(mat)):
        if(mat[i][i] != 1):
            isNotIdenty = True
            break
        for j in range(0, len(mat[i])):
            if(j == i): continue
            if(mat[i][j] != 0):
                isNotIdenty = True
                break
    return isNotIdenty

#Pruebe a usar la matriz "Mat" para comprobar si es identidad
mat = manager.createMatrix(4, 4)
daMat = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0 ,1, 0], [0, 0, 0, 1]]

print(f"La matriz es identidad: {not checkMat(daMat)}")
A_Manager.printMatrix(daMat)