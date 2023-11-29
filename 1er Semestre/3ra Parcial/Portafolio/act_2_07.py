import random

def randomInt(min:int, max:int)->int:
    return random.randint(min, max)

def createMatrix(n:int, m:int):
    mat:list = []
    for i in range(0, n):
        mat_2:list = []
        mat.append(mat_2)
        for j in range(0, m):
            mat[i].append(randomInt(0, 1))
    return mat

def printVec(mat):
    text:str = ""
    for i in range(0, len(mat)):
        text = f"{text}["
        for j in range(0, len(mat[i])):
            text = f"{text}{mat[i][j]}, "
        text = f"{text}]\n"
    print(text)

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

mat = createMatrix(4, 4)
daMat = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0 ,1, 0], [0, 0, 0, 1]]

print(f"La matriz es identidad: {not checkMat(daMat)}")
printVec(daMat)