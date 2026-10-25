#Ordenamiento de 3 números dados por el usuario
#Jose Gabriel Orosco
#19 de octubre
t=[]
print("")
for i in range(3):
    m=int(input("Ingrese un número"))
    t.append(m)
def lo(r):
    for pasa in range(len(r) - 1):
        for i in range(len(r) - 1 - pasa):
            if r[i] > r[i + 1]:
                temp = r[i]
                r[i] = r[i + 1]
                r[i + 1] = temp
    return (r)
lr=lo(t)
print("El resultado es: ",lr)