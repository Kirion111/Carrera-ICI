from guizero import App, Text, PushButton, TextBox

# Obtener el promedio de n personas preguntando su año de nacimiento y asumiendo que el año actual es 2023

j:int = 0
n:int = 0
suma:int = 0
a_actual:int = 2023

def getAmount():
    global j, n
    if(amount.value != '' and not amount.value.isalpha() and amount.value.isnumeric() and int(amount.value) > 0):
        n = int(amount.value)
        message.value = f"Dame el {j + 1}° año de nacimiento"
        amount.value = ""
        btnn.visible = False
        ages.visible = True
    else:
        App.info(daApp,title="Error:", text="Ingrese un numero valido")

def giveResult():
    global j, n, suma
    ValueCheck = False
    if(amount.value != '' and not amount.value.isalpha() and amount.value.isnumeric() and int(amount.value) > 0 and int(amount.value) < a_actual):
        suma = suma + (a_actual - int(amount.value))
        j = j + 1
        message.value = f"Dame el {j + 1}° año de nacimiento"
        amount.value = ""
        if(j >= n):
            message.value = "¿Cuantas edades quieres promediar?"
            App.info(daApp,title="Resultado:", text=f"El promedio de las edades es es:\n {suma/n}")
            ages.visible = False
            btnn.visible = True
            n = 0
            j = 0
            suma = 0
    else:
        if(amount.value == ''):
            App.info(daApp,title="Error:", text="Ingrese un numero valido")
        else:
            if(int(amount.value) <= 0):
                App.info(daApp,title="Error:", text="Edad invalida (No puede ser menor o igual a 0)")
            else: 
                if(int(amount.value) >= a_actual):
                    App.info(daApp,title="Error:", text="Edad invalida (No puede ser mayor o igual al año actual)") 
                else:
                 App.info(daApp,title="Error:", text="Edad invalida")

daApp = App("Edad promedio", 500, 150, 'auto')

message = Text(daApp,text="¿Cuantas edades vas a promediar?")
amount = TextBox(daApp, width=50, text="")
btnn = PushButton(daApp, command=getAmount, text="Ingresar")
ages = PushButton(daApp, command=giveResult, text="Agregar edad")
ages.visible = False

daApp.display()