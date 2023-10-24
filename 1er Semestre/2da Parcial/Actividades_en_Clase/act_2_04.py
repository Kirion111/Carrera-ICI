from guizero import App, Text, PushButton, TextBox

daApp = App("Aplicación", 500, 200, 'auto')

def guiveResult():
    resultado = str(int(numero.value)**2)
    App.info(daApp,title="Resultado", text=str(resultado))

message = Text(daApp,text="Dame un numero")
numero = TextBox(daApp, width=50, text="")

btnn = PushButton(daApp, command=guiveResult, text="Calcular")

daApp.display()