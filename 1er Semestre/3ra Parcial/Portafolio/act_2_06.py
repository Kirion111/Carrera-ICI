from arrayManager import arrayManager as A_Manager
manager = A_Manager()

manager.defineRange(1, 100)
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

mat = manager.createMatrix(n, m)
A_Manager.printMatrix(mat)
suma = 0

for i in range(0, len(mat)):
    for j in range(0, len(mat[i])):
        suma = suma + mat[i][j]

print(f"La suma de los elementos de la matriz es: {suma}")
