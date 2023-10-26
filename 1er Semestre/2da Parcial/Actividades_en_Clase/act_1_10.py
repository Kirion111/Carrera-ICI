from guizero import App, Text, PushButton, TextBox

# Una empresa desea calcular el sueldo total de una persona bajo los siguientes rubros;
# Aumentos: Sueldo base, 5% de canasta basica y 3% de prima de antiguedad
# Reducciones: Si el sueldo base excede los 10,000 pesos, el ISR será del 30%, menos de esta cantidad, hará que el ISR sea de el 20%
# Indique cuanto es de la nomina, y cuanto el patrón debe pagar al SAT

sueldo_base:int | float = 0
salario:int | float = 0
canasta_basica:float = 0.05
prima_antiguedad:float = 0.03
nomina:int | float = 0
impuesto:float = 0

def getIncome():
    global sueldo_base, salario, canasta_basica, prima_antiguedad, nomina, impuesto

    isr:float = 0.0

    validValue = income.value != '' and not income.value.isalpha() and income.value.isnumeric() and float(income.value) > 0
    if(validValue):
        sueldo_base = float(income.value)
        salario = sueldo_base + (sueldo_base * canasta_basica) + (sueldo_base * prima_antiguedad)

        if(sueldo_base > 10000):
            isr = 0.3
        else:
            isr = 0.2

        impuesto = impuesto + (sueldo_base * isr)
        nomina = nomina + salario
        message.value = "Desea agregar el sueldo de otro empleado?"
        income.value = ""
        add.visible = True
        end.visible = True
        btnn.visible = False
        income.visible = False
    else:
        App.info(daApp,title="Error:", text="Ingrese un salario valido")

def addIncome():
    message.value = "Ingrese el sueldo base del empleado"
    income.visible = True
    end.visible = False
    add.visible = False
    btnn.visible = True

def endIt():
    App.info(daApp,"Resultado:", f"La nomina total es de: {nomina}\nEl impuesto en total es de: {impuesto}")
    daApp.destroy()



daApp = App("Empresa generica", 500, 150, 'auto')
message = Text(daApp,text="Ingrese su sueldo base")
income = TextBox(daApp, width=50, text="")
btnn = PushButton(daApp, command=getIncome, text="Ingresar")
add = PushButton(daApp, command=addIncome, text="Agregar otro empleado")
end = PushButton(daApp, command=endIt, text="Terminar y Calcular")
add.visible = False
end.visible = False


daApp.display()