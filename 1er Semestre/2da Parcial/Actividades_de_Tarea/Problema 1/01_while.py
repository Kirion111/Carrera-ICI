i:int = 0
tot:int = 0
n:int = 0

while(n <= 0):
    n=int(input("¿Numeros a sumarse?\n"))
    if(n <= 0):
        print("El numero debe ser mayor a 0")

while(i < n):
    j = (i + 1) * 2
    tot = tot + j
    i = i + 1

print("La suma de los primeros", n, "numeros pares es:", tot)