#Llenar un arreglo con los números primos comprendidos
#entre 1 y 100 y los muestre en 
#pantalla en orden ascendente.
#Jose Gabriel Orosco
bom=[]
numero=1
n=100
for i in range(2,n+1):
    contador=0
    for j in range(1,n+1):
     if i%j==0:
      contador+=1
    if contador==2:
     bom.append(i)
for pasa in range(len(bom)-1):
    for i in range(len(bom)-1-pasa):
        if bom[i]>bom[i+1]:
            temp=bom[i]
            bom[i]=bom[i+1]
            bom[i+1]=temp
print(bom)
        
   
