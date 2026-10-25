#¿Cuál es el último factor primo del número 600851475143 ?
r=[]
for i in range(2,600851475143):
    p=600851475143%i
    if 600851475143%i==0:
        r.append(i)
        print(r)
'''n=600851475143
i=2
while i*i<n:
    while n%i==0:
        n=n/i
    i=i+1
print(n)'''