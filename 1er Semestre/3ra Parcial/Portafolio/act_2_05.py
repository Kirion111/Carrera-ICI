from arrayManager import arrayManager
aManager = arrayManager()

aManager.defineRange(1, 100)
arr = aManager.createArray(int(input("Ingresa el tamaño del arreglo: ")))

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