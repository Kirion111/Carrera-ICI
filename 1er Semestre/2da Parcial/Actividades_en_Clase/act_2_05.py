from guizero import App, Text, PushButton, TextBox
import pyttsx3

engine = pyttsx3.init()

daApp = App("Aplicación", 500, 200, 'auto')

def guiveResult():
    resultado = str(int(numero.value)**2)
    engine.say(f"El cuadrado de{int(numero.value)} es {resultado}")
    engine.runAndWait()

message = Text(daApp,text="Dame un numero")
result = Text(daApp, text="")
numero = TextBox(daApp, width=50, text="")

btnn = PushButton(daApp, command=guiveResult, text="Calcular")

daApp.display()