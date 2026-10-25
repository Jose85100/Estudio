#Función que extrae la dimensón de la ultima palabra de una cadena
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()

"""pal=input("Ingrese su string")

def cal(pal):
    p = []
    for c in pal[::-1]:
        if c !=" ":
            p.append(c)
        else:
            break
    k=len(p)
    return (k)
print("El tamaño de la ultima palabra es", cal(pal))"""