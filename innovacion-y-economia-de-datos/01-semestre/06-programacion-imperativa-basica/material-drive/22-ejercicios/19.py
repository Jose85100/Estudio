#Escribir un programa que calcule el capital producido por un capital de x de pesos, al cabo de 
#un año depositado a un interés del y% mensual.
cap=int(input("Ingrese el capital"))
inr=int(input("Ingrese el interés mensual"))
capprod=((cap*inr)/100)*12
captot=cap+capprod
print("Capital producido", capprod)
print("Capital total", captot)
