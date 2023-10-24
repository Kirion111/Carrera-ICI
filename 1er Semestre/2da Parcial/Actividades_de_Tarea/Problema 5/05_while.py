i:int = 0
tot:int = 0
n1:int = 0
n2:int = 0

while(n1 <= 0):
    n1=int(input("Escribe el 1er numero a multiplicarse\n"))
    if(n1 <= 0):
        print("El numero debe ser mayor a 0")

while(n2 <= 0):
        n2=int(input("Escribe el 2do numero a multiplicarse\n"))
        if(n2 <= 0):
            print("El numero debe ser mayor a 0")

while(i < n2):
    tot = tot + n1
    i = i + 1

print(f"El producto de {n1} y {n2} es de: {tot}")