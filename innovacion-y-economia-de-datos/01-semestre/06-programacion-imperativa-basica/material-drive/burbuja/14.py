#Llenar un arreglo con 20 números y luego busque un número especifico.
#Jose Gabriel Orosco
bom=[]
mo=0
for i in range(0,20):
    p=int(input("Ingrese un número"))
    bom.append(p)
for pasa in range(len(bom)-1):
    for i in range(len(bom)-1-pasa):
        if bom[i]>bom[i+1]:
            temp=bom[i]
            bom[i]=bom[i+1]
            bom[i+1]=temp
im=int(input("Que elemento desea buscar? "))
k=bom.index(im)
print("está en la posición", bom.index(im))
print(bom[k])
