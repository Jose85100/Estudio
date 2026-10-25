#Leer 5 números por teclado, los copie a otro arreglo multiplicados por 2 y muestre el 
#segundo arreglo
m_1=[]
num=[]
for i in range(0,6):
    ir=int(input("Ingresar los números"))
    m_1.append(ir)
    
for i in m_1:
    l=i*2
    num.append(l)
    
for pasa in range(len(num)-1):
    for i in range(len(num)-1-pasa):
        if num[i]>num[i+1]:
            temp=num[i]
            num[i]=num[i+1]
            num[i+1]=temp

print(num)
    
