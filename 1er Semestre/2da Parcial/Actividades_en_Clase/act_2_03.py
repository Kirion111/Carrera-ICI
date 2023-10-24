from guizero import App, Text, PushButton, TextBox

daApp = App("Aplicación", 500, 200, 'auto')

def guiveResult():
    result.value = (f"El cuadrado es: {str(int(numero.value)**2)}")

message = Text(daApp,text="Dame un numero")
numero = TextBox(daApp, width=50, text="")
result = Text(daApp, text="")

btnn = PushButton(daApp, command=guiveResult, text="Calcular")

daApp.display()