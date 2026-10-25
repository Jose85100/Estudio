#Programa que simule el funcionamniento de una calculadora
#Jose Gabriel Orosco
#19/08/2021
num_1=int(input("Ingrese el numero 1"))
num_2=int(input("Ingrese el numero 2")) 
print("1. Suma")
print("2. Resta")
print("3. División")
print("4. Multiplicación")
num_o=int(input("Qué desea realizar?"))

if num_o==1:
    print(num_1+num_2)
elif num_o==2:
    print(num_1-num_2)
elif num_o==3:
    print(num_1/num_2)
elif num_o==4:
    print(num_1*num_2)
    

