#muestre los números del 1 al 100 en una tabla de 10x10.
#Jose Gabriel Orosco 
"""cont=0
for i in range(0,101):
    print(i, end=" ")
    if i==cont:
       print('\n')
       cont=cont+10"""
ll=[]
cont=10
for i in range(1,101):
    ll.append(i)
for i in ll:
    print(i, end=" ")
    if i==cont:
        print('\n')
        cont=cont+10
    
