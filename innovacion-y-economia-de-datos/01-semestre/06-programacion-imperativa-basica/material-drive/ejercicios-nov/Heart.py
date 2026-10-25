#Código dibujar función cardioide
#3/11/2021

from sympy import *
from sympy.plotting import plot_parametric
import math

#%matplotlib inline

t = symbols('t')
a=1

r = a* ((sin(t)* sqrt(abs(cos(t))))/(sin(t) + 7/5) - 2* sin(t) + 2)


print ("Corazon 4")
plot_parametric( r*cos(t), r*sin(t), (t, 0, 2*pi))

