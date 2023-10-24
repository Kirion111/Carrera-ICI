from guizero import App, Text, PushButton, TextBox

# Crea una calculadora funcional que puda sumar, restar, multiplicar y dividir al seleccionar el tipo de operación y pedir 2 numeros para dichas ecuaciones .

j:int = 0
def createArray(lenght:int)->list:
    arr:list = []
    for i in range(0, lenght):
        arr.append(0)

    return arr

def getNumbers():
    global j, numbers

    validInfo = number.value != '' and not number.value.isalpha() and number.value.isnumeric()
    if(validInfo):
        valifNumber = float(number.value) > 0

    if(validInfo and valifNumber):
        numbers[j] = float(number.value)
        message.value = "Ingresa el segundo numero"
        number.value = ""
        j = j + 1
        if(j >= 2):
            daApp.height = 275
            message.value = f"¿Que operacion quieres realizar?\n(Tus numeros son: {numbers[0]} y {numbers[1]})"
            btnn.visible = False
            number.visible = False
            for i in range(0, len(options)):
                options[i].visible = True

def doIncrease():
    global j, numbers
    App.info(daApp, title="Resultado:", text=f"La suma es: {numbers[0] + numbers[1]}")

def doDecrease():
    global j, numbers
    App.info(daApp, title="Resultado:", text=f"La resta es: {numbers[0] - numbers[1]}")

def doProduct():
    global j, numbers
    App.info(daApp, title="Resultado:", text=f"La multiplicacion es: {numbers[0] * numbers[1]}")

def doDivision():
    global j, numbers
    App.info(daApp, title="Resultado:", text=f"La division es: {numbers[0] / numbers[1]}")

def reset():
    global j, numbers
    j = 0
    numbers = createArray(2)
    message.value = "Ingresa el primer numero"
    daApp.height = 125
    btnn.visible = True
    number.visible = True
    for i in range(0, len(options)):
        options[i].visible = False

numbers:list() = createArray(2)
options:list() = createArray(5)
opt_text:list() = ["Sumar", "Restar", "Multiplicar", "Dividir", "Reiniciar"]
opt_funct:list() = [doIncrease, doDecrease, doProduct, doDivision, reset]

daApp = App("Calculadora", 500, 125, 'auto')
message = Text(daApp,text="Ingresa el primer numero")
number = TextBox(daApp, width=50, text="")
btnn = PushButton(daApp, command=getNumbers, text="Ingresar")

for i in range(0, len(options)):
    options[i] = PushButton(daApp, command=opt_funct[i], text=opt_text[i])
    options[i].visible = False

daApp.display()