#Programa que simule el funcionamniento de una calculadora
#Jose Gabriel Orosco
#02/09
import os
from time import sleep
op=0
while op!=5:
    os.system('cls')
    print("========================")
    print("||Calculadora")
    print("||1. Suma")
    print("||2. Resta")
    print("||3. División")
    print("||4. Multiplicación")
    print("||5. Salir")
    op=0
    op=int(input("Elija una opción "))
    if op==5:
        break
    num_1=int(input("Ingrese el numero 1 "))
    num_2=int(input("Ingrese el numero 2 ")) 
    if op==1:
        print("||",num_1,"+",num_2,"=",num_1+num_2)
    elif op==2:
        print("||",num_1,"-",num_2,"=",num_1-num_2)
    elif op==3:
        if num_2>0 or num_2<0:
            print("||",num_1,"/",num_2,"=",num_1/num_2)
        elif num_2==0:
            print("No se pude dividir en cero")
    elif op==4:
        print("||",num_1,"*",num_2,"=",num_1*num_2)
    sleep(1)
    input("Ingrese una tecla para continuar")
    
