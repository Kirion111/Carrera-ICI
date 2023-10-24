from guizero import App, Text, PushButton

#obtén la suma de todos los cuadrados de los numeros pares entre 0 y 20 consecutivos
cua:int = 0
daApp = App("Cuadrados", 500, 150, 'auto')

for i in range(0, 21, 2):
    cua = cua + (i ** 2)

message = Text(daApp,text=f"\n\nLa suma de los cuadrados de los numeros pares entre 0 y 20 es:\n {cua}")

daApp.display()