import random

def randomInt(min:int, max:int)->int:
    return random.randint(min, max)

def createArray(lenght:int)->list:
    arr:list = []
    for i in range(0, lenght):
        arr.append(randomInt(0, 100))

    return arr

arr = createArray(int(input("Ingresa el tamaño del arreglo: ")))

text:str = "["
print(f"Inicio: {arr}")
for i in range(0, len(arr)):
    passNum:int = arr[len(arr) - 1]
    for j in range(len(arr) -1, i, -1):
        if j <= i:break
        arr[j] = arr[j-1]
    arr[i] = passNum
    text += f"{arr[i]}, "
text += "]"
#print(text)
print(f"Final: {arr}")