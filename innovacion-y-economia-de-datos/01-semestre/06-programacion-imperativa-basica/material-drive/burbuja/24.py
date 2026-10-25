#¿Cuál es el número positivo más pequeño que es divisible por 
#todos los números del 1 al 20?
#Encuentra la diferencia entre la suma de los cuadrados de
#los primeros 100 números 
#naturales y el cuadrado de la suma.
t = 20
cont=0
de=0
num=[]
for i in range(1,2520):
    for j in range(1,21):
        if i%j==0:
            cont=cont+1
        if cont==20:
            num.append(i)
            print(num)
    cont=0
num_2=[]
sumc=0
sumn=0
for i in range(0,101):
    j=i**2
    num_2.append(j)
for i in num_2:
    sumc=sumc+i

for i in range(0,101):
    sumn=sumn+i
print("La diferencia es: ", (sumn**2)-sumc)

               


    
