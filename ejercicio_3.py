# Programa que pida numero de dias y calcule la conversion a horas y minutos
numero = int(input("ingrese numero de dias: "))

horas = 24 * numero 
minutos = 60 * horas
print(f"{numero} días equivalen a {horas} horas o {minutos} minutos.")