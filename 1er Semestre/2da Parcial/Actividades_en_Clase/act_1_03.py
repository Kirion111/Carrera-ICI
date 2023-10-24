from guizero import App, Text, PushButton, TextBox

# Se desea saber la cantidad de alumnos que pasaron la materia, son 25 y la calificación aprobatoria es de 7
alumnos:int = 25
j:int = 0
alumn_aprob:int = 0

def getGrades():
    global j, alumnos, alumn_aprob
    if(result.value != '' and not result.value.isalpha() and result.value.isnumeric() and int(result.value) >= 0 and int(result.value) <= 10):
        if(int(result.value) >= 7):
            alumn_aprob = alumn_aprob + 1

        result.value = ""
        j = j + 1
        message.value = f"Escribe la calificacion del alumno no. {j + 1}°"
        if (j >= alumnos):
            message.value = ""
            App.info(daApp, title="Resultado", text=f"La cantidad de alumnos que pasaron la materia es de {alumn_aprob}")
            j = 0
            alumn_aprob = 0
    else:
        App.info(daApp,title="Error:", text="Ingrese un numero valido")

daApp = App("Evaluación", 500, 150, 'auto')
message = Text(daApp,text=f"Escribe la calificacion del alumno no. {j + 1}°")
result = TextBox(daApp, width=40 ,text="")
btnn = PushButton(daApp, command=getGrades, text="agregar calificacion")

daApp.display()