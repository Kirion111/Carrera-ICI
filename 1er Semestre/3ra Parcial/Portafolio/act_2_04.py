from arrayManager import arrayManager as A_Manager
manager = A_Manager()

manager.defineRange(1, 100)
arr = manager.createArray(4)
max = 0
min = 0

print(f"El arreglo es: {arr}")

for i in range(0, len(arr)):
    if i < 1:
        max = arr[i]
        min = arr[i]
    else:
        if(arr[i] > max):
            max = arr[i]
        if(arr[i] < min):
            min = arr[i]

print(f"El valor maximo es {max}\nEl valor minimo es {min}")



