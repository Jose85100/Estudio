cantidad=5
ArregloFrutas=[]
Tem=[]
print(f"por favor ingresar {cantidad} frutas")
for l in range(cantidad):
    fruta=str(input("Ingrese la fruta"))
    ArregloFrutas.append(fruta)
print("sus datos son", ArregloFrutas)
for i in range (1,cantidad-1):
              for j in range(1,cantidad-1-i):
                  if ArregloFrutas[i]>ArregloFrutas[i+1]:
                      temp=ArregloFrutas[i]
                      ArregloFrutas[i]=ArregloFrutas[i+1]
                      ArregloFrutas[i+1]=temp
                    
print("Arreglo ordenado", ArregloFrutas)
