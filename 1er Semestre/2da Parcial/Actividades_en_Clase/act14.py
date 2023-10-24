from guizero import App, Text, PushButton, TextBox

# La tienda "bronkos" debe vender productos a n alumnos; ofrecen : tortas, tacos, hot dogs y pizzas
# Imprime los productos vendidos en total.

i:int = 0
alumnos:int = 0
tortas:int = 0
tacos:int = 0
hotdogs:int = 0
pizzas:int = 0

def setAlltoDefault():
    global i, alumnos, tortas, tacos, hotdogs, pizzas

    i = 0
    alumnos = 0
    tortas = 0
    tacos = 0
    hotdogs = 0
    pizzas = 0

def setAmount():
    global alumnos, i

    validInfo = number.value != '' and not number.value.isalpha() and number.value.isnumeric()
    if(validInfo):
        validNumber = int(number.value) > 0

    if(validInfo and validNumber):
        alumnos = int(number.value)
        message.value = f"¿Que desea comprar cliente {i+1}?\n(1 = torta, 2 = tacos, 3 = hotdog, 4 = pizza)"
        compra.visible = True
        btnn.visible = False
        number.value = ""
    else:
        if(not validInfo):
            App.info(daApp, title="Error:", text="Ingrese un numero valido")
        elif(not validNumber):
            App.info(daApp, title="Error:", text="Ingrese un numero del 1 al 4")

def buyItem():
    global alumnos, tortas, tacos, hotdogs, pizzas

    validInfo = number.value != '' and not number.value.isalpha() and number.value.isnumeric()
    if(validInfo):
        validNumber = int(number.value) > 0 and int(number.value) < 5
    
    if(validInfo and validNumber):
        n:int = int(number.value)
        match n:
            case 1:
                tortas = tortas + 1
            case 2:
                tacos = tacos + 1
            case 3:
                hotdogs = hotdogs + 1
            case 4:
                pizzas = pizzas + 1
            case _:
                App.info(daApp, title="Error:", text="Ingrese un numero valido")

        message.value = f"¿Desea comprar otro producto cliente {i+1}?\n(1 = si, 0 = no)"   
        number.value = ""
        choice.visible = True
        compra.visible = False 

    else:
        if(not validInfo):
            App.info(daApp, title="Error:", text="Ingrese un numero valido")
        elif(not validNumber):
            App.info(daApp, title="Error:", text="Ingrese un numero del 1 al 4")

def guiveChoice():
    global i, alumnos

    validInfo = number.value != '' and not number.value.isalpha() and number.value.isnumeric()
    if(validInfo):
        validNumber = int(number.value) >= 0 and int(number.value) <= 1

    if(validInfo and validNumber):
        daChoice:int = int(number.value)
        match daChoice:
            case 0:
                i = i + 1
                if(i < alumnos):
                    message.value = f"¿Que desea comprar cliente {i+1}?\n(1 = torta, 2 = tacos, 3 = hotdog, 4 = pizza)"
                    compra.visible = True
                    choice.visible = False
                    number.value = ""
                else:
                   
                    compra.visible = False
                    choice.visible = False
                    btnn.visible = True
                    number.value = ""
                    App.info(daApp, title="Vent total:", text=f"Tortas: {tortas}\nTacos: {tacos}\nHotdogs: {hotdogs}\nPizzas: {pizzas}")
                    message.value = f"¿Cuantos alumnos comprarán en la tienda?"
                    setAlltoDefault()
            case 1:
                    message.value = f"¿Que desea comprar cliente {i+1}?\n(1 = torta, 2 = tacos, 3 = hotdog, 4 = pizza)"
                    compra.visible = True
                    choice.visible = False
                    number.value = ""
    else:
        if(not validInfo):
            App.info(daApp, title="Error:", text="Ingrese un numero valido")
        elif(not validNumber):
            App.info(daApp, title="Error:", text="Ingrese un numero del 1 al 4")


daApp = App("Tienda bronkos", 420, 130, "auto")
message = Text(daApp, text="¿Cuantos alumnos comprarán en la tienda?")
number = TextBox(daApp, width=50, text="")
btnn = PushButton(daApp, command=setAmount, text="Ingresar")
compra = PushButton(daApp, command=buyItem, text="Ingresar compra")
choice = PushButton(daApp, command=guiveChoice, text="Aceptar")
compra.visible = False
choice.visible = False
daApp.display()
