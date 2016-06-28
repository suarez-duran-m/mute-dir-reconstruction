#
#
# Mute versión 2D
#
#
# Consideremos dos paneles paralelos de dimensiones NBar x NBar, separados una distancia $D$ (medida en cm) conformados
# con un entramdo de barras, cada una con un ancho $d$ (medida en cm)
#
#
import numpy as np
import matplotlib.pyplot as plt
# Pregunto por las caracteristicas de los paneles
# NBar = input("Numero de Barras ? ")
NBar = 10
#
# AnchBar = input("Ancho de las Barras (cm) ? ")
AnchBar = 5 # cm
#
# Pregunto por la separación de los paneles
# SeparacionPaneles = input("Separacion de los Paneles (cm) ? ")
SeparacionPaneles = 10 # cm
#
# Dibujo el detector
# Defino los 2 paneles
PArriba = np.zeros((NBar,NBar)) # i j
PAbajo = np.zeros((NBar,NBar)) # k l
#
plt.subplot(1, 2, 1)
plt.imshow(PArriba)
plt.subplot(1, 2, 2)
plt.imshow(PAbajo)
# dibujo los paneles
plt.show()
#
#Dirección de Arribo en cm
Xingresocm = 10
Yingresocm = 25
# Direccion de arribo adimensionalizada
XingresoAd=Xingresocm/AnchBar
YingresoAd=Yingresocm/AnchBar
# Cambio a las coordenadas naturales del detector
XingresoBar=XingresoAd +(NBar-1)/2 +1
YingresoBAR=-YingresoAd +(NBar-1)/2 +1
#
print XingresoAd, YingresoAd, XingresoBar, YingresoBAR

for i in range(NBar)  :
    for j in range(NBar)  :
        if i+XingresoAd < NBar  and i+XingresoAd >= 0 :
            if j+YingresoAd < NBar  and j +YingresoAd >= 0 :
                PArriba[i,j]= 10.
                PAbajo[i+XingresoAd,j+YingresoAd]= 10.
                print XingresoAd, YingresoAd , i+XingresoAd, -i, j+YingresoAd, -j, "Pij ", i,j, PArriba[i,j],"Pkl ", i+XingresoAd,j+YingresoAd, PAbajo[i+XingresoAd,j+YingresoAd]
            else :continue
        else : continue
#
plt.subplot(1, 2, 1)
plt.imshow(PArriba)
plt.subplot(1, 2, 2)
plt.imshow(PAbajo)
#
plt.show()

