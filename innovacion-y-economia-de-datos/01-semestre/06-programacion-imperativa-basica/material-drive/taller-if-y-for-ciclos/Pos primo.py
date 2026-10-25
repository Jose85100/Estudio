#Busgar el número primo en la posición 999
#Jose Gabriel Orosco
prim=[]
ran=[2]
par=0
for i in range(2,10000):
    for n in ran :
    
        if i % 2 != 0:
            prim.append(i)
        
print("El número primo en la posición 999, es", prim[999])

