#Leer una cadena texto y decir cuantas mayusculas hay.
#Jose Gabriel Orosco
p=str(input("Ingrese una palabra o frase "))
nim=[]
a=0
b=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
c=0
for i in p:
    nim.append(i)
for j in nim:
    if i in b:
        a+=1
print(f"Hay {a} mayusculas")

        

