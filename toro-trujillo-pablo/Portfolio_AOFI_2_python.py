edad = 0
nombre = 0
print ("¿Cual es tu edad?")
edad = int(input ())
if edad > 17:
	print("A delante")
	print ("Y... ¿Cual es tu nombre?")
	var_nombre = input ()
	print ("Saludos", var_nombre)
else:
	print ("No se puede pasar, solo mayores de edad")
print ("¡Hasta pronto!")