#programa que solicite al usuario su peso en kilogramos y su altura en metros
kilogramos = float(input("ingrese el peso en kilogramos: "))

altura = float(input("ingrese la altura en metros: "))
imc = kilogramos/altura **2 
print(f"el indice de masa corporal es: {imc} kg/m**2")
