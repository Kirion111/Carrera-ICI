array = [1, 3, 5, 7, 9, 11]
numero_a_buscar = 5
repeticiones = 0

resultado = "No se encuentra el número en el array"

for i in range(len(array)):
    if array[i] == numero_a_buscar:
        resultado = "Sí se encuentra el número en el array"
        repeticiones += 1
        break

print(f"{resultado}, aparece {repeticiones} veces dentro del array.")