import time
comida1 = 0
comida2 = 0
dia = 0
almuerzo = {}
cena = {}
semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

print ("¿Que vas a comer durante la semana?")
for dia in semana:
	print ("Que quieres para almorzar el ", dia, "?")
	comida = input ()
	almuerzo[dia] = comida
	print ("Que quieres para cenar el ", dia, "?")
	comida = input()
	cena[dia] = comida

print ("Tu menu es:")
for dia in semana:
	print (dia, " - Almuerzo: ", almuerzo[dia], " , Cena: ", cena[dia])
	time.sleep (1)