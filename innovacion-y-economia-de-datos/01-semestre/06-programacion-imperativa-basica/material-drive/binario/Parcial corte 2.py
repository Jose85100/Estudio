#Parcial programación imperativa
#Segundo corte
#Programa que encuentra la diferencia entre la suma de los
#cuadrados de los primeros 100 números naturales y el cuadrado
#de la suma
#12 Octubre
#Jose Gabriel Orosco
m=0
n=0

"""a=0
s=0"""
for i in range(1,101):
    p=i**2
    m=m+p
    n=n+i
print("El número es",(n**2)-m)

#Alternativa
"""
def sumo(n):
    a=0
    s=0
    for j in range(1,n+1):
        p=j**2
        a=a+p
        s=s+j
    return (s**2)-a

print(sumo(100))"""
        
 
