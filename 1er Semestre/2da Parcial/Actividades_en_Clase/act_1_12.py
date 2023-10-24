from guizero import App, Text, PushButton

# Genera la siguiente secuencia, de forma infinita: 0101010101...

i:int = 0

#La funcion after nos permite llamar a una funcion despues de un determinado tiempo
#Si se llama a si mismo, se crea un ciclo, como si fuera un while

def start():
    message.value = "Secuencia:\n"
    btnn.visible = False
    daApp.height = 60
    daApp.after(15, cycles)

def cycles():
    global i
    i = i + 1
    if(i % 44 == 0 and i != 0):
        message.value = message.value + "\n"
        daApp.height = int(60 + (18 * (i / 44)))

    message.value = message.value + "01"
    daApp.after(15, cycles)

daApp = App("Generador binario infinito", 800, 150, "auto")
message = Text(daApp, text="ADVERTENCIA\n Esta secuencia es infinita,en el momento en que usted haga click en este botón\nse generará la secuencia sin fin\ny tendrá que cerrar el programa manualmente para terminar con el bucle")
btnn = PushButton(daApp, command=start, text="Iniciar secuencia")
daApp.display()

