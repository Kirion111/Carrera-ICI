
count:int = 0
matriz =   [[1, 3, 5, 7, 9, 11],
            [2, 4, 6, 8, 10, 12],
            [1, 3, 5, 7, 9, 11],
            [2, 4, 6, 8, 10, 12]]

numero_a_buscar = 11
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == numero_a_buscar:
            count += 1
print(f"El no. {numero_a_buscar}; se encontro {count} veces")