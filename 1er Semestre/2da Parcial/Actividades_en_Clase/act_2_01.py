from guizero import App, Text, PushButton

daApp = App("Aplicación", 500, 200, 'auto')

message = Text(daApp,text="Bienvenido")

def daButtonEvent():
    message.value = "Hola mundo"

daButton = PushButton(daApp, text="Decir hola", command=daButtonEvent)
daApp.display()
