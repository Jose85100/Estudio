#Leer una cadena texto y decir cuantas vocales hay.

#Jose Gabriel Orosco
p=str(input("Ingrese una palabra o frase"))
nim=[]
a=0
for i in p:
    nim.append(i)
#no me recibe j en in
for j in nim:
    if j=='a'or j=='e'or j=='i'or j=='o' or j=='u' or j=='í' or j=='á' or j=='é' or j=='ú' or j=='ó'or j=='A'or j=='E'or j=='I'or j=='O'or j=='U':
        a=a+1
        
print("El total de vocales es: ", a)

        
    
