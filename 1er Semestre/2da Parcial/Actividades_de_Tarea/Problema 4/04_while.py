i:int = 0
tot=0
n:int = 0

while(n <= 0):
    n=int(input("¿Cuantos numeros numeros al cubo se van a sumar entre si?\n"))
    if(n <= 0):
        print("El numero debe ser mayor a 0")

while(i < n):
    j = i + 1
    tot = tot + (j*j*j)
    i = i + 1

print(f"El producto de los {n} primeros numeros es: {tot}")