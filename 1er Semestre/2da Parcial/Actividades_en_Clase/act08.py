from guizero import App, Text, PushButton, TextBox

#Dado el año de nacimiento, indique cuatos años va a cumplir una persona el siguiente año

result:int = 0

def getAge():
    global result
    validYear = year.value != '' and not year.value.isalpha() and year.value.isnumeric() and int(year.value) > 0
    validAge = age.value != '' and not age.value.isalpha() and age.value.isnumeric() and int(age.value) > 0

    if(validYear and validAge):
        ValidInfo = int(year.value) >= int(age.value)

    if(validYear and validAge and ValidInfo):
        result = int(year.value) - int(age.value)
        App.info(daApp,title="Resultado:", text=f"El año que viene cumpliras {result + 1} años")
    else:
        if(not validYear):
            App.info(daApp,title="Error:", text="Ingrese un Año valido")
        elif(not validAge):
            App.info(daApp,title="Error:", text="Ingrese un Año de nacimiento valido")
        elif(not ValidInfo):
            App.info(daApp,title="Error:", text="El año actual no puede ser menor al año de nacimiento")

daApp = App("Años que va a cumplir", 300, 150, "auto")
message = Text(daApp, text="Ingresa el año actual")
year = TextBox(daApp, width=30, text="")
message = Text(daApp, text="Ingresa tu año de nacimiento")
age = TextBox(daApp, width=30, text="")
btnn = PushButton(daApp, command=getAge, text="Calcular")

daApp.display()
