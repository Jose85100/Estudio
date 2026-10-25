print("1. De Celsius a Fahrenheit")
print("2. De Fahrenheit a Celsius")
op=int(input("Elija una opción"))
if op==1:
    t=int(input("Ingrese la temperatura en grados Celsius"))
    f=(t*(9/5))+32
    print(f)
elif op==2:
    t2=int(input("Ingrese la temperatura en fahrenheit"))
    c=(t2-32)*5/9
    print(c)
else:
    print("A bueno")
