Multiplicación de matrices
#Mauricio Arana Jiemenez
#Sep 2021

# LEER MATRIZ A
datosm1 = float()
datosm2 = float()
f = float()
c = float()
f1 = float()
c1 = float()
print("Digite el número de filas de la matriz A ")
f = int(input())
print("Digite el número de columnas de la matriz A ")
c = int(input())
a = [[float() for ind0 in range(c)] for ind1 in range(f)]
i = 1
j = 1
for i in range(1,f+1):
	for j in range(1,c+1):
		print("Digite el dato para la fila ",i," columna ",j, " ", end="")
		datosm1 = int(input())
		a[i-1][j-1] = datosm1
i = 1
j = 1
# Escribir los datos de la matriz llena
print("La matriz A es : ")
for i in range(1,f+1):
	for j in range(1,c+1):
		print(a[i-1][j-1]," ", end="")
	print("")
# LEER MATRIZ B
print("Digite el número de filas de la matriz B ")
f1 = int(input())
print("Digite el número de columnas de la matriz B ")
c1 = int(input())
b = [[float() for ind0 in range(c1)] for ind1 in range(f1)]
i = 1
j = 1
for i in range(1,f1+1):
	for j in range(1,c1+1):
		print("Digite el dato para la fila ",i," columna ",j, " ", end="")
		numero = int(input())
		b[i-1][j-1] = numero
i = 1
j = 1
# Escribir los datos de la matriz llena
print("La matriz B es : ")
for i in range(1,f1+1):
	for j in range(1,c1+1):
		print(b[i-1][j-1]," ", end="")
	print("")
# MULTIPLICACION DE LAS DOS MATRICES
matc = [[float() for ind0 in range(c1)] for ind1 in range(f)]
n = int()
k = int()
k = 1
n = f
print("La matriz Resultado es : ")
for i in range(1,f+1):
	for j in range(1,c1+1):
		matc[i-1][j-1] = 0
		for k in range(1,n+1):
			matc[i-1][j-1] = matc[i-1][j-1]+(a[i-1][k-1]*b[k-1][j-1])
		print(matc[i-1][j-1]," ", end="")
	print("")