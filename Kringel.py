import numpy as np
from scipy.special import fresnel
import matplotlib.pyplot as plt
import gmsh
import sys
import math

gmsh.initialize()

t = np.linspace(0, 3 , 100) #erzeugt 5 Punkte (letzter Eintrag) von 0-5 (ersten zwei Einträge)
sin, cos = fresnel(t) #fresnelintegral erzeugen
x = (sin)  #vergrößert allesum Faktor 100
y = (cos) 

z = t * 0 #verschiebung in z
b = z + 0.1 #breite
dicke = 0.01

resultdx = [] #arrays für die Koordinaten der Normalenvektoren
resultdy = []

#Funktion für die Normalenvektoren
def mach_Span():
    for idx in range(len(x)-1):
        x0, y0, xn, yn = x[idx], y[idx], x[idx+1], y[idx+1]
        dx, dy = xn-x0, yn-y0
        norm = math.hypot(dx, dy) * 1/dicke
        dx /= norm
        dy /= norm
        xc = x0-dy
        yc = y0+dx
        resultdx.append(xc)
        resultdy.append(yc)


plt.plot(x,y,'green') #Graph erzeugen
plt.show()
mach_Span()

#x,y,zGMSH Koordinaten in einzelne Arrays
coordsx = (x)
resultx = []
for x in coordsx:
    resultx.append(x)
        
coordsy = (y)
resulty = []
for y in coordsy:
    resulty.append(y)
        
coordsz = (z)
resultz = []
for z in coordsz:
    resultz.append(z)

coordsb = (b)
resultb =[]
for b in coordsb:
    resultb.append(b) 
    
#Koordinaten zusammenfügen
coords = list(zip(resultx, resulty, resultz))

coordsb = list(zip(resultx, resulty, resultb))

coordsd = list(zip(resultdx, resultdy, resultz))

coordsdb = list(zip(resultdx, resultdy, resultb))

#über jede Koordinatenpackung iterieren
for [x,y,z] in coords:
        gmsh.model.geo.addPoint(x, y, z)

#dem ganzen ding eine Breite geben
for [x,y,b] in coordsb:
        gmsh.model.geo.addPoint(x, y, b)
        
for [xc,yc,z] in coordsd:
        gmsh.model.geo.addPoint(xc, yc, z)

for [xc,yc,b] in coordsdb:
        gmsh.model.geo.addPoint(xc, yc, b)
  
gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(1)
gmsh.write("Kringel.msh")
# start with empty model again
gmsh.fltk.run()
gmsh.clear()
gmsh.finalize()
