import random

def randomInt(min:int, max:int)->int:
    return random.randint(min, max)

def createMatrix(n:int, m:int):
    mat:list = []
    for i in range(0, n):
        mat_2:list = []
        mat.append(mat_2)
        for j in range(0, m):
            mat[i].append(randomInt(0, 100))
    return mat
n = 0
m = 0

while n <= 0:
    n = int(input("Ingresa el numero de filas: "))
    if n <= 0:
        print("El numero de filas debe ser mayor a 0")

while m <= 0:
    m = int(input("Ingresa el numero de columnas: "))
    if m <= 0:
        print("El numero de columnas debe ser mayor a 0")

mat = createMatrix(n, m)
suma = 0

for i in range(0, len(mat)):
    for j in range(0, len(mat[i])):
        suma = suma + mat[i][j]

print(f"La suma de los elementos de la matriz es: {suma}")
