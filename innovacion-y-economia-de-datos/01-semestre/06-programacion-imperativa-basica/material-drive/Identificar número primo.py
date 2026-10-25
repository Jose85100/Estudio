num=int(input("Ingresar el número a identificar"))
print(num)
for n in range(2,num):
    if num%n==0:
        print("No es primo")
    else:
        print("Es primo")
