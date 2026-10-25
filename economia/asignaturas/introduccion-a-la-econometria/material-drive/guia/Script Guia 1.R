#Script guía 1
#30/01/2023
# Ejecutar desde una carpeta que contenga dda.xls (véase README).
dir(pattern = "*.xls")
#package - readxl - permite leer hojas de cálculo
library(readxl) #Activa paquetes descargados
base = read_excel("dda.xls") #importa la base de datos

base$dx #permite ver los campos de la bs
attach(base) #observar campos ind de la bs 
dx
View(base)

#Estadísticas descriptivas
mean(dx)
sd(dx)
sum(dx)
summary(dx)

library(pastecs)
stat.desc(dx)

#Gráficos
hist(dx, col="red")
hist(dx, col="red", main = "Histograma de demanda")
plot(px,dx) #x hotizontal y vertical

#Correlación
cor(dx,px)
cor(base)
cov(dx,px) #coinciden con el signo
cov(base)
