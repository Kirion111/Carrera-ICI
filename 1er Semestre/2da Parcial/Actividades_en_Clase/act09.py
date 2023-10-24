from guizero import App, Text, PushButton, TextBox

# Obtenga la suma de 5 numeros capturados entre [5, 10] inclusive
lim:int = 5
i:int = 0
result:int | float = 0

def getValue():
    global result, i, lim
    validInfo = number.value != '' and not number.value.isalpha() and number.value.isnumeric()
    if(validInfo):
        validNumber = int(number.value) >= 5 and int(number.value) <= 10

    if(validInfo and validNumber):
        result = result + int(number.value)
        i = i + 1
        message.value = f"Vamos a sumar 5 numeros entre 5 y 10\nIngresa el {i + 1}° numero"
        number.value = ""
        if(i >= lim):
            App.info(daApp,title="Resultado:", text=f"La suma de los numeros es: {result}")
            i = 0
            number.value = ""
            message.value = f"Vamos a sumar 5 numeros entre 5 y 10\nIngresa el {i + 1}° numero"
    else:
        if(not validInfo):
            App.info(daApp,title="Error:", text="Ingrese un numero valido")
        elif(not validNumber):
            App.info(daApp,title="Error:", text="Ingrese un valor entre 5 y 10")

daApp = App("Suma con limite", 500, 150, 'auto')
message = Text(daApp,text=f"Vamos a sumar 5 numeros entre 5 y 10\nIngresa el {i + 1}° numero")
number = TextBox(daApp, width=50, text="")
btnn = PushButton(daApp, command=getValue, text="Ingresar")


daApp.display()