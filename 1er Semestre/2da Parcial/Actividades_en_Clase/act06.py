from guizero import App, Text, PushButton, TextBox

#Obtenga la suma de todos los cuadrados de n numeros capturados del teclado

j:int = 0
n:int = 0
tot:int | float = 0

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
    global j, tot, n
    if(number.value != '' and not number.value.isalpha() and number.value.isnumeric() and int(number.value) > 0):
        tot = tot + (float(number.value) ** 2)
        j = j + 1
        message.value = f"Ingrese el {j + 1}° numero"
        number.value = ""
        if(j >= n):
            message.value = "¿Cuatos numeros vas a ingresar?"
            App.info(daApp,title="Resultado:", text=f"La suma de los cuadrados es: {tot}")
            j = 0
            n = 0
            tot = 0
            result.visible = False
            btnn.visible = True
    else:
        App.info(daApp,title="Error:", text="Ingrese un valor valido")
            
daApp = App("Cuadrados", 500, 150, 'auto')
message = Text(daApp,text="¿Cuatos numeros vas a ingresar?")
number = TextBox(daApp, width=50, text="")
btnn = PushButton(daApp, command=getAmount, text="Ingresar")
result = PushButton(daApp, command=doSquare, text="Calcular")
result.visible = False


daApp.display()