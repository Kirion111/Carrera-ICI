import random
class arrayManager:

    def __init__(self):
        self.da_data = []
        self.daMin = 0
        self.daMax = 0

    def defineRange(self, min:int, max:int):
        self.daMin = min
        self.daMax = max

    def randomInt(min:int, max:int)->int:
        return random.randint(min, max)

    def createArray(self,lenght:int):
        arr:list = []
        for i in range(0, lenght):
            arr.append(arrayManager.randomInt(self.daMin, self.daMax))
        return arr

    def createMatrix(self, rows:int, columns:int):
        mat:list = []
        for i in range(0, rows):
            mat_2:list = []
            mat.append(mat_2)
            for j in range(0, columns):
                mat[i].append(arrayManager.randomInt(self.daMin, self.daMax))
        return mat
    
    def printMatrix(mat:list):
        text:str = ""
        for i in range(0, len(mat)):
            text = f"{text}["
            for j in range(0, len(mat[i])):
                text = f"{text}{mat[i][j]}, "
            text = f"{text}]\n"
        print(text)