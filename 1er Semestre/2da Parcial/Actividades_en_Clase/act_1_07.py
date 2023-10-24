from guizero import App, Text, PushButton, TextBox

#Capture n numeros enteros positivos y obtenga la suma del cuadrado de los pares y el cubo de los impares

j:int = 0
n:int = 0
tot_even:int | float = 0
tot_odd:int | float = 0

def getAmount():
    global n

    if(number.value != '' and not number.value.isalpha() and number.value.isnumeric() and int(number.value) > 0):
        n = int(number.value)
        message.value = f"Ingrese el {j + 1}° numero"
        number.value = ""
        btnn.visible = False
        result.visible = True
    else:
        App.info(daApp,title="Error:", text="Ingrese un valor valido")

def doSquare():
    global j, tot_even, tot_odd, n
    if(number.value != '' and not number.value.isalpha() and number.value.isnumeric() and int(number.value) > 0):
        if(int(number.value) % 2 == 0):
            tot_even = tot_even + (float(number.value) ** 2)
        else:
            tot_odd = tot_odd + (float(number.value) ** 3)

        j = j + 1
        message.value = f"Ingrese el {j + 1}° numero"
        number.value = ""
        if(j >= n):
            message.value = "¿Cuatos numeros vas a ingresar?"
            App.info(daApp,title="Resultado:", text=f"La suma de los cuadrados de los numeros pares es: {tot_even}\nLa suma de los cubos de los numeros impares es de: {tot_odd}")
            j = 0
            n = 0
            tot = 0
            result.visible = False
            btnn.visible = True
    else:
        App.info(daApp,title="Error:", text="Ingrese un valor valido")
            
daApp = App("Cuadrados y cubos", 500, 150, 'auto')
message = Text(daApp,text="¿Cuatos numeros vas a ingresar?")
number = TextBox(daApp, width=50, text="")
btnn = PushButton(daApp, command=getAmount, text="Ingresar")
result = PushButton(daApp, command=doSquare, text="Calcular")
result.visible = False


daApp.display()