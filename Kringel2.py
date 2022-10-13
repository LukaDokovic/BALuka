import numpy as np
from scipy.special import fresnel
import matplotlib.pyplot as plt
import gmsh
import sys
import math
import os


gmsh.initialize()

#gmsh.merge('./Analogieprüfstand_Spanraum.STEP')


Zoom = 1
Anzahl = 10
t = np.linspace(0, 1, Anzahl+1) #erzeugt 5 Punkte (letzter Eintrag) von 0-5 (ersten zwei Einträge)
sin, cos = fresnel(t) #fresnelintegral erzeugen
x = ((sin)*Zoom) 
y = ((cos)*Zoom) 
z = t * 0 #verschiebung in z
b = z + 0.5 #breite
dicke = 0.01
lc = 1e-2

resultdx = [] #arrays für die Koordinaten der Normalenvektoren
resultdy = []

#Funktion für die Normalenvektoren
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



index = 5000
index2 = 6000








#über jede Koordinatenpackung iterieren
for [x,y,z] in (coords[:-1]):
        gmsh.model.geo.addPoint(x, y, z, lc, index)
        index+=1

#dem ganzen ding eine Breite geben
for [x,y,b] in (coordsb[:-1]):
        gmsh.model.geo.addPoint(x, y, b, lc, index2)
        index2+=1
        
for [xc,yc,z] in coordsd:
        gmsh.model.geo.addPoint(xc, yc, z, lc)

for [xc,yc,b] in coordsdb:
        gmsh.model.geo.addPoint(xc, yc, b, lc)
  
  
gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(1)
gmsh.write("Kringel.msh")
# start with empty model again
gmsh.fltk.run()
gmsh.clear()
gmsh.finalize()
