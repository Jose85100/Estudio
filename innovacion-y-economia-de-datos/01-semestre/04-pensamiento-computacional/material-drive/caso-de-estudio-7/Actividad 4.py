pab = input("Ingrese palabra: ")
mayusculas=0
for j in pab:
    if j.isupper() == True:
        mayusculas +=1

print("Total mayusculas: " , mayusculas)
