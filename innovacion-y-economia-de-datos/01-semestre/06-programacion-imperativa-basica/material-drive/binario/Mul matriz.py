def pom(u):
	datosm1 = float()
	datosm2 = float()
	f = float()
	c = float()
	f1 = float()
	c1 = float()
	print("Digite el número de filas de la matriz ", u)
	f = int(input())
	print("Digite el número de columnas de la matriz ", u)
	c = int(input())

	y = [[float() for ind0 in range(c)] for ind1 in range(f)]
	i = 1
	j = 1
	for i in range(1,f+1):
		for j in range(1,c+1):
			print("Digite el dato para la fila ",i," columna ",j, " ", end="")
			datosm1 = int(input())
			y[i-1][j-1] = datosm1
	i = 1
	j = 1
	return (y)
a=pom("a")
b=pom("b")

print("este es a", a,"este es b", b)

def multi(m1,m2):
	if len(m1[0]) == len(m2):
		m3=[]
		for i in range(len(m1)):
			m3.append([])
			for j in range(len(m2[0])):
				m3[i].append(0)
		for i in range(len(m1)):
			for j in range(len(m2[0])):
				for k in range(len(m1[0])):
					m3[i][j]+=m1[i][k]*m2[k][j]
		return m3
	else:
		return None
RES = multi(a,b)
if RES==None:
	print("No se pueden multiplicar las matrices")
else:
	for fila in RES:
		print("[", end=" ")
		for elemento in fila:
			print(elemento,end=" ")
		print("]")