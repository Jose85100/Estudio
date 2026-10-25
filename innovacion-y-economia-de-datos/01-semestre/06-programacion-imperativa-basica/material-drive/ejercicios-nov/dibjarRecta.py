import matplotlib.pyplot as plt

def media(x):
  return sum(x) / len(x)

def varianza(x):
  suma = 0
  for i in x:
    suma += i ** 2
  return suma / len(x) - media(x) ** 2
def covarianza(x, y):
  suma = 0
  for i in range(len(x)):
    suma += x[i] * y[i]
  return suma / len(x) - media(x) * media(y)
def recta_regresion(x, y):
  b = covarianza(x, y) / varianza(x)
  a = media(y) - b * media(x)
  return a, b

def dibuja_recta_regresion(x, y):
  fig, ax = plt.subplots()
  ax.scatter(x, y)
  a, b = recta_regresion(x, y)
  ax.plot([min(x), max(x)], [a + b * min(x), a + b * max(x)], color = 'red')
  return ax
x = [1, 2, 3, 4, 5, 6]
y = [20, 18, 12, 10, 9, 9]
dibuja_recta_regresion(x, y)
plt.savefig('RectaDispersion.png')
