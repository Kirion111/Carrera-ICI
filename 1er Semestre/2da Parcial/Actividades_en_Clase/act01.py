from guizero import App, Text, PushButton, TextBox

# Sacar el promedio de n numeros leidos del teclado

j:int = 0        
suma:float = 0
n:int = 0

def getAmount():
    global j, n

    if (amount.value != '' and not amount.value.isalpha() and amount.value.isnumeric() and int(amount.value) > 0):
        n = int(amount.value)
        message.value = f"Dame el {j + 1}° Numero a promediar"
        amount.value = ""
        btnn.visible = False
        calcular.visible = True
    else:
        App.info(daApp,title="Error:", text="Ingrese un numero valido")

def getResult():
    global suma, j, n

    if(amount.value != ''and not amount.value.isalpha() and (amount.value.isnumeric() or amount.value.isdecimal) and float(amount.value) > 0):
        j = j + 1
        message.value = f"Dame el {j+1}° numero: a promediar"
        suma = suma + float(amount.value)
        amount.value = ""
        if(j >= n):
           message.value = "¿Cuantos numeros quieres promediar?"
           App.info(daApp,title="Resultado:", text=f"El promedio es: {suma/n}")
           calcular.visible = False
           btnn.visible = True
           j = 0
           n = 0
           suma = 0
    else:
        App.info(daApp,title="Error:", text="Ingrese un numero valido")
    

daApp = App("Promedio", 500, 150, 'auto')

message = Text(daApp,text="¿Cuantos numeros quieres promediar?")
amount = TextBox(daApp, width=50, text="")
btnn = PushButton(daApp, command=getAmount, text="Ingresar")
calcular = PushButton(daApp, command=getResult, text="Calcular")
calcular.visible = False

daApp.display()