import numpy as np
from scipy.special import fresnel
import matplotlib.pyplot as plt
import gmsh
import sys
import math
import os


gmsh.initialize()

gmsh.open('./Analogieprüfstand_Spanraum.STEP')

Zoom = 70
Anzahl = 100
t = np.linspace(0.38, 3, Anzahl+1) #erzeugt 5 Punkte (letzter Eintrag) von 0-5 (ersten zwei Einträge)
sin, cos = np.sqrt(fresnel(t)) #fresnelintegral erzeugen
x = ((sin)*Zoom)-7.46
y = ((cos)*Zoom)-38
z = t * 0 #verschiebung in z
b = z - 23 #breite
dicke = 1
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


index1 = 100
index2 = 200
index3 = 300
index4 = 400


#über jede Koordinatenpackung iterieren
for [x,y,z] in (coords[:-1]):
        gmsh.model.geo.addPoint(x, y, z, lc, index1)
        index1+=1

for i in range(Anzahl-1):
    gmsh.model.geo.addLine(index1-1,index1-2)
    index1-=1

#dem ganzen ding eine Breite geben
for [x,y,b] in (coordsb[:-1]):
        gmsh.model.geo.addPoint(x, y, b, lc, index3)
        index3+=1

for i in range(Anzahl-1):
    gmsh.model.geo.addLine(index3-1,index3-2)
    index3-=1
        
for [xc,yc,z] in coordsd:
        gmsh.model.geo.addPoint(xc, yc, z, lc, index2)
        index2+=1

for i in range(Anzahl-1):
    gmsh.model.geo.addLine(index2-1,index2-2)
    index2-=1

for [xc,yc,b] in coordsdb:
        gmsh.model.geo.addPoint(xc, yc, b, lc, index4)
        index4+=1
  
for i in range(Anzahl-1):
    gmsh.model.geo.addLine(index4-1,index4-2)
    index4-=1
    
#Punktwolke verbinden
gmsh.model.geo.addSpline([index1-1,index2-1])
gmsh.model.geo.addSpline([index2-1,index4-1])
gmsh.model.geo.addSpline([index3-1,index4-1])
gmsh.model.geo.addSpline([index3-1,index1-1])
  
gmsh.model.geo.addSpline([(index1-2)+Anzahl,(index2-2)+Anzahl])
gmsh.model.geo.addSpline([(index2-2)+Anzahl,(index4-2)+Anzahl])
gmsh.model.geo.addSpline([(index3-2)+Anzahl,(index4-2)+Anzahl])
gmsh.model.geo.addSpline([(index3-2)+Anzahl,(index1-2)+Anzahl])  

gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(1)
gmsh.write("Kringel.msh")
# start with empty model again
gmsh.fltk.run()
gmsh.clear()
gmsh.finalize()
