from guizero import App, Text, PushButton, TextBox

daApp = App("Aplicación", 500, 200, 'auto')

message = Text(daApp,text="Aplicación")
nombre = TextBox(daApp, width=50)

daApp.display()