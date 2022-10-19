import numpy as np
from scipy.special import fresnel
import matplotlib.pyplot as plt
import gmsh
import sys
import math
import os

Spandau = gmsh.model.occ
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
        Spandau.addPoint(x, y, z, lc, index1)
        index1list.append(index1)
        index1+=1
"""
for i in range(Anzahl-1):
    Spandau.addSpline([index1-1,index1-2])
    index1-=1
"""
print("index1list = ",index1list)
Spandau.addBSpline(index1list, degree=2)


#dem ganzen ding eine Breite geben
for [x,y,b] in (coordsb[:-1]):
        Spandau.addPoint(x, y, b, lc, index3)
        index3list.append(index3)
        index3+=1
    
Spandau.addBSpline(index3list, degree=2)

for [xc,yc,z] in coordsd:
        Spandau.addPoint(xc, yc, z, lc, index2)
        index2list.append(index2)
        index2+=1

Spandau.addBSpline(index2list, degree=2)

for [xc,yc,b] in coordsdb:
        Spandau.addPoint(xc, yc, b, lc, index4)
        index4list.append(index4)
        index4+=1
 
Spandau.addBSpline(index4list,degree=2)
  

#Punktwolke verbinden
Spandau.addSpline([index1-1,index2-1])
Spandau.addSpline([index2-1,index4-1])
Spandau.addSpline([index3-1,index4-1])
Spandau.addSpline([index3-1,index1-1])


#fester Span 
Spandau.addPoint(dicke,0,0,lc,70)
Spandau.addPoint(dicke,0,b,lc,71)
Spandau.addPoint(0,0,b,lc,72)
Spandau.addLine(70,71)
Spandau.addLine(71,72)
Spandau.addPoint(1,2.5,b,lc,73)

norm2 = 1/np.sqrt(1+np.square(2.5))
Spanx = dicke * (-2.5*norm2)
Spany = dicke * (1*norm2)
Spandau.addPoint(1-Spanx,2.5-Spany,0,lc,74)
Spandau.addPoint(1-Spanx,2.5-Spany,b,lc,75)

abstand = (np.sqrt(np.square(resultx[0]-1)+np.square(resulty[0]-2.5)))/2
vektorx = norm2*abstand
vektory = norm2*abstand*2.5
Spandau.addPoint(1+vektorx, 2.5+vektory,0,lc,76)
Spandau.addPoint(1+vektorx, 2.5+vektory,b,lc,77)


Spandau.synchronize()
gmsh.model.mesh.generate(1)
gmsh.write("Kringel.msh")
gmsh.fltk.run()
gmsh.clear()
gmsh.finalize()
