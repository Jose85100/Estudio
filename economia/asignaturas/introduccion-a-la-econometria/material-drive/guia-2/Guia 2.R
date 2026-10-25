#Guía 2 Regresión simple
# Ejecutar desde una carpeta que contenga dda.xls (véase README).
library(readxl)
bd=read_excel("dda.xls")
attach(bd)
plot(px,dx)

#Regresión simple
modelodx=lm(dx~px) #vardep~varindp
summary(modelodx)
plot(px,dx)
abline(modelodx,col="red")
library(stargazer)
stargazer(modelodx,type="text",out="m1.doc")
stargazer(modelodx,type="text",out="m1.xls")


anova(modelodx)

#Errores
errores=residuals(modelodx) #ui
dxgorro=fitted(modelodx) #y^
cbind(dx, dxgorro,errores)
