from guizero import App, Text, PushButton, TextBox

# Preguntar un numero, y en base de eso, asumir que dia de la semana es

n:int = 0

def getDay():
    global n

    validInfo = day.value != '' and not day.value.isalpha() and day.value.isnumeric()
    if(validInfo):
        validNumber = int(day.value) > 0 and int(day.value) < 8

    if(validInfo and validNumber):
        n = int(day.value)

        match n:
            case 1:
                App.info(daApp, title="Dia:", text="Es lunes")
            case 2:
                App.info(daApp, title="Dia:", text="Es Martes")
            case 3:
                App.info(daApp, title="Dia:", text="Es Miercoles")
            case 4:
                App.info(daApp, title="Dia:", text="Es Jueves")
            case 5:
                App.info(daApp, title="Dia:", text="Es Viernes")
            case 6:
                App.info(daApp, title="Dia:", text="Es Sabado")
            case 7:
                App.info(daApp, title="Dia:", text="Es Domingo")
            case _: 
                App.info(daApp, title="Dia:", text="Ingrese un numero valido")
    else:
        if(not validInfo):
            App.info(daApp, title="Error:", text="Ingrese un numero valido")
        elif(not validNumber):
            App.info(daApp, title="Error:", text="Ingrese un numero del 1 al 7")


daApp = App("Dia de la semana", 420, 180, "auto")
message = Text(daApp, text="Ingrese un numero del 1 al 7\nCon eso asumiremos qe dia de la semana es")
day = TextBox(daApp, width=50, text="")
btnn = PushButton(daApp, command=getDay, text="Ingresar")
daApp.display()