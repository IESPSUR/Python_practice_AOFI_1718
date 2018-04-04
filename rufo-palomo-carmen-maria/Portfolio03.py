var_numero1 = 0
var_numero2 = 0
var_numero3 = 0

print ("Dime un número mayor que 0")
var_numero1 = int(input ())
if var_numero1 > 0:
	print ("Dime otro número, pero esta vez que sea mayor al primero")
	var_numero2 = int(input())
	if var_numero2 > var_numero1:
		print("Por último, dime un número menor que 0")
		var_numero3 = int(input())
		if var_numero3 < 0:
			print (var_numero1, "+", var_numero2, "+", var_numero3, "=", var_numero1+var_numero2+var_numero3)
		else:
			print ("¡Hasta luego!")
	else:
		print ("¡Hasta luego!")
else:
	print ("¡Hasta luego!")
