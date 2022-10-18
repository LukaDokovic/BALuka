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
Anzahl = 50
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


index1 = 1000
index1list=[]
index2 = 2000
index2list=[]
index3 = 3000
index3list=[]
index4 = 4000
index4list=[]


#über jede Koordinatenpackung iterieren
for [x,y,z] in (coords[:-1]):
        gmsh.model.occ.addPoint(x, y, z, lc, index1)
        index1list.append(index1)
        index1+=1
        
for i in range(Anzahl-1):
    gmsh.model.occ.addSpline([index1-1,index1-2])
    index1-=1

#gmsh.model.occ.addSpline(index1list)


#dem ganzen ding eine Breite geben
for [x,y,b] in (coordsb[:-1]):
        gmsh.model.occ.addPoint(x, y, b, lc, index3)
        index3list.append(index3)
        index3+=1

for i in range(Anzahl-1):
    gmsh.model.occ.addSpline([index3-1,index3-2])
    index3-=1
      
#gmsh.model.occ.addSpline(index3list)

for [xc,yc,z] in coordsd:
        gmsh.model.occ.addPoint(xc, yc, z, lc, index2)
        index2list.append(index2)
        index2+=1

for i in range(Anzahl-1):
    gmsh.model.occ.addSpline([index2-1,index2-2])
    index2-=1

#gmsh.model.occ.addSpline(index2list)

for [xc,yc,b] in coordsdb:
        gmsh.model.occ.addPoint(xc, yc, b, lc, index4)
        index4list.append(index4)
        index4+=1

for i in range(Anzahl-1):
    gmsh.model.occ.addSpline([index4-1,index4-2])
    index4-=1
  
#gmsh.model.occ.addSpline(index4list)

  

#Punktwolke verbinden
gmsh.model.occ.addSpline([index1-1,index2-1])
gmsh.model.occ.addSpline([index2-1,index4-1])
gmsh.model.occ.addSpline([index3-1,index4-1])
gmsh.model.occ.addSpline([index3-1,index1-1])


gmsh.model.occ.synchronize()
gmsh.model.mesh.generate(1)
gmsh.write("Kringel.msh")
gmsh.fltk.run()
gmsh.clear()
gmsh.finalize()
