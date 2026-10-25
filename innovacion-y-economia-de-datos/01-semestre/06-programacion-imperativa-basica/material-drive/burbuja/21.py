#Leer una cadena de texto que esta encriptada con
#suma de tres en el código ASCII y 
#mostrarla desencriptada
#Jose Gabriel Orosco
n=int(input("Ingrese el número de caracteres"))
pe=[]
for i in range(n):
    po=int(input("Ingrese el código"))
    pe.append(po)
for i in pe:
    print(chr(i-3), end=" ")
