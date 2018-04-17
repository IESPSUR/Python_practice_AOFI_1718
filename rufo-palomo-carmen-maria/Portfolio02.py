var_edad = 0
var_nombre = ""

print ("¿Cual es tu edad?")
var_edad = int(input ())
if var_edad < 18:
	print ("El programa es sólo para mayores de edad")
else: 
	print ("¿Como te llamas?")
	var_nombre = input ()
	print ("Hola", var_nombre)
print ("¡Hasta pronto!")