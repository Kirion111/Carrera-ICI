lista:list = []
suma:int = 0
n:int = 0

while(n <=0):
    n = int(input("¿Cuantas calificaciónes va a evaluar?\n"))
    if(n <=0):
        print("No puedes evaluar 0 o menos calificaciónes")

for i in range(0, n):
    lista.append(int(input(f"Ingrese la calificación {i + 1}:\n")))
    suma = suma + lista[i]

print("las calificaciónes fueron: ")
for i in range(0, n):
    print(f"calificación {i + 1}: {lista[i]}")

print(f"El promedio de {n} calificaciones es de {suma/n}")