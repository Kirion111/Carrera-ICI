i:int = 0
tot=1
n:int = 0

while(n <= 0):
    n=int(input("¿Cuantos numeros van a multiplicarse entre si?\n"))
    if(n <= 0):
        print("El numero debe ser mayor a 0")

while(i < n):
    j = i + 1
    tot = tot * j
    i = i +1

print(f"El producto de los {n} primeros numeros es: {tot}")