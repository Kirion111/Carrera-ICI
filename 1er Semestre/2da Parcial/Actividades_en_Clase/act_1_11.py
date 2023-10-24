from guizero import App, Text, PushButton, TextBox

# Genera la siguiente secuencia: 01010101... finitas veces

n:int = 0

def setAumount():
    global n
    n = int(number.value)
    secuence:str = ""
    for i in range (0, n):
        if(n >= 24):
            # El != 0 es para evitar que se pierda el primer 01 y se quede solo, desalineando la secuencia
            if(i % 23 == 0 and i != 0):
                secuence = secuence + "\n"
                daApp.height = int(180 + (17 * (i / 22)))
        else:
            daApp.height = 180

        secuence = secuence + "01"

    outPut.value = f"\nSecuencia:\n{secuence}"
    outPut.visible = True

daApp = App("Generador binario", 420, 180, "auto")
text = Text(daApp, text="Cuantas veces deseas que se repita la secuancia '01'?")
number = TextBox(daApp, width=50, text="")
btnn = PushButton(daApp, command=setAumount, text="Ingresar")
outPut = Text(daApp, text=f"")
outPut.visible = False

daApp.display()