#Programa que verifica los números recurrentes vs los resultados
#4/11
#Jose Gabriel Orosco

p=[1,4,5,20,30,41]
j=[]
for i in range(1,7):
    k=int(input("Ingrese los números"))
    j.append(k)
def verificar(p,j):
    l=0
    gana=0
    falla=0
    for i in p:
        if i==j[l]:
            print(i,"Coincidió")
            l+=1
            gana+=1
        elif i!=j[l]:
            print(i,"El número no coincidió")
            l+=1
            falla+=1
    if gana==6:
        print('Ganó el baloto!!!')
    else:
        print('No ganó')


verificar(p,j)