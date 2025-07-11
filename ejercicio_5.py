#programa que permita al usuario elegir si desea convertir de Celsius a Fahrenheit o de Fahrenheit a Celsius
opcion = int(input("ingrese 1 para convertir grados celsius a fahrenheit o 2 para convertir fahrenheit a celsius"))
if opcion == 1:
    C = float(input("ingrese la temperatura en celsius: "))
    F = C * 1.8+32 
    print(f"{C} ºC equivalen a {F:.2f} ºF ")
elif opcion == 2:
    F = float(input("ingrese la temperatura en fahrenheit: "))
    C = (F-32)/1.8
    print(f"{F} ºF equivalen a {C:.2f} ºC ")
else:
    print("no valido: ")
    