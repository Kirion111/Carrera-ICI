i:int = 0
tot=1
n:int = 0

while(n <= 0):
    n=int(input("¿Cuantos numeros par van a multiplicarse entre si?\n"))
    if(n <= 0):
        print("El numero debe ser mayor a 0")

for i in range(0, n):
    j = (i + 1)*2
    tot = tot * j

print(f"El producto de los {n} primeros numeros es: {tot}")