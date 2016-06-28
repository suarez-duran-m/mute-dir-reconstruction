#
#
# Mute versión 2D
#
#
# Consideremos dos paneles paralelos de dimensiones NBar x NBar, separados una distancia $D$ (medida en cm) conformados con un entramdo de barras, cada una con un ancho $d$ (medida en cm)
#
#
import numpy as np
import matplotlib.pyplot as plt
#
def DireccionArribo(XPixelArriba, YPixelArriba, XPixelAbajo, YPixelAbajo)

    return XArribo, YArribo, ZArribo
#
def VAlidoPixel(XPixel, YPixel, NBar)
    if XPixel < 0 and XPixel > NBar :
        print " error en Pixel X  "
        break
    else: continue
    if YPixelArriba < 0 and YPixelArriba > NBar :
        print " error en Pixel Y  "
        break
    else: continue
    return
#
# Pregunto por las caracteristicas de los paneles
# NBar = input("Numero de Barras ? ")
# AnchBar = input("Ancho de las Barras (cm) ? ")
# SeparacionPaneles = input("Separacion de los Paneles (cm) ? ")
NBar = 10
AnchBar = 5 # cm
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
plt.imshow(PAbaMpo)
# dibujo los paneles
plt.show()
#
# Pixel arriba
XPixelArriba= 10
YPixelArriba= 10
#
# Valido la entrada

# Pixel arriba
XPixelAbajo= 10
YPixelAbajo= 10
#
#
# Direccion de arribo
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

