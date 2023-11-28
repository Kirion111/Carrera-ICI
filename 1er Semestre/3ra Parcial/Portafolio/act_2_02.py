array = [7, 3, 5, 7, 9, 7]
numero_a_buscar = 7
repeticiones = 0

resultado = "No se encuentra el número en el array"
info = ""

for i in range(len(array)):
    if array[i] == numero_a_buscar:
        repeticiones += 1
        resultado = "Se encontro el numero"
        info = info + f"{i}, "
if(info != ""):
    print(f"{resultado}, se repite {repeticiones} veces el No. {numero_a_buscar}, en las posiciones {info}")
else:
    print(resultado)