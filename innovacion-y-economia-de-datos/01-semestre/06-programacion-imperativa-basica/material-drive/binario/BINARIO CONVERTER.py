#Convertidor de binario a decimal y viceversa
#Jose Gabriel Orosco
print("1.Binario to decimal")
print("2. Decimal to binario")
"""pe=int(input("Ingrese qué tipo de número va a convertir\n"))"""
po=1
while po!=0:
    pe = int(input("Ingrese qué tipo de número va a convertir\n"))
    if pe==1:
        m = int(input("Ingrese el número"))
        print(int(str(m),2))
    if pe==2:
        n=int(input("Ingrese el número"))
        temp=format(n,"b")
        print(bin(n))
        print(temp)
po=int(input("0 Salir, 1 Continuar"))
