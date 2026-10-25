#Imprimir asteriscos
#Jose Gabriel Orosco
#26/08
num =int(input("Ingrese el número"))
for numer in range(num):
    espa=num-numer-1
    asteriscos=1+numer*2
    print(" "*espa+"*"*asteriscos)


"""
Prototipos
for i in range(num):
  # print(i)
  print(' ' * (num - i - 1) + "*" * (2 * i + 1))

num = 10

for i in range(num):
  # print(i)
  print(' ' * (num - i - 1) + "*" * (2 * i + 1))"""
