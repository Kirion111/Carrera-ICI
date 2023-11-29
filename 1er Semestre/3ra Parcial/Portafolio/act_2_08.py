import random

def randomInt(min:int, max:int)->int:
    return random.randint(min, max)

def createMatrix(empty:bool, n:int, m:int):
    mat:list = []
    for i in range(0, n):
        mat_2:list = []
        mat.append(mat_2)
        for j in range(0, m):
            if empty:
                mat[i].append(0)
            else:
                mat[i].append(randomInt(1, 10))
    return mat

def printVec(mat):
    text:str = ""
    for i in range(0, len(mat)):
        text = f"{text}["
        for j in range(0, len(mat[i])):
            text = f"{text}{mat[i][j]}, "
        text = f"{text}]\n"
    print(text)
    
n = 4
mat1 = createMatrix(False, n, n)
mat2 = createMatrix(False, n, n)
finalMat = createMatrix(True, n, n)

print("Matrices 1 y 2: \n")
printVec(mat1)
printVec(mat2)

for i in range(0, len(mat1)):
    for j in range(len(mat1[i])):
        finalMat[i][j] = mat1[i][j] + mat2[i][j]

print("Matriz final: \n")
printVec(finalMat)