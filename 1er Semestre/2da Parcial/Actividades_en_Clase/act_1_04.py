from guizero import App, Text, PushButton, TextBox

# Calcula el cuadrado de un numero positivo leido desde el teclado

def getSquare():
    if(number.value != '' and not number.value.isalpha() and number.value.isnumeric() and int(number.value) > 0):
        App.info(daApp,title="Resultado:", text=f"El cuadrado de {number.value} es {int(number.value) ** 2}")
    else:
        App.info(daApp,title="Error:", text="Ingrese un valor valido")

daApp = App("El cuadrado", 500, 150, 'auto')
message = Text(daApp,text="Ingresa un numero positivo")
number = TextBox(daApp, width=50, text="")
btnn = PushButton(daApp, command=getSquare, text="Calcular")

daApp.display()