import numpy as np
from scipy.special import fresnel
import gmsh
import sys
import math
import os
Spandau = gmsh.model.occ
gmsh.initialize()
gmsh.open('./Analogieprüfstand_Spanraum.STEP')

Zoom = 70
Anzahl = 50
Start = 0.38
Ende = 3
xVerschiebung = -7.47
yVerschiebung = -38
t = np.linspace(Start, Ende, Anzahl+1) #erzeugt 5 Punkte (letzter Eintrag) von 0-5 (ersten zwei Einträge)
sin, cos = np.sqrt(fresnel(t)) #fresnelintegral erzeugen
x = ((sin)*Zoom)+xVerschiebung
y = ((cos)*Zoom)+yVerschiebung
z = t * 0 #verschiebung in z
b = z - 23 #breite
dicke = 1
lc = 1e-2

resultdx = [] #arrays für die Koordinaten der Normalenvektoren
resultdy = []

#Funktion für die Normalenvektoren
for idx in range(len(x)-1):
    x0, y0, x1, y1 = x[idx], y[idx], x[idx+1], y[idx+1]
    dx = x1-x0
    dy = y1-y0
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




#Vom Span aus Rückwärts
tSpan1 = Start - 0.01
sinSpan1, cosSpan1 = np.sqrt(fresnel(tSpan1)) #fresnelintegral erzeugen
xSpan1 = ((sinSpan1)*Zoom)+xVerschiebung
ySpan1 = ((cosSpan1)*Zoom)+yVerschiebung
Spandau.addPoint(xSpan1,ySpan1,0,lc,80)
Spandau.addPoint(xSpan1,ySpan1,b,lc,81)

#Normalenvektor
tSpan = np.linspace(Start - 0.01, Start, 2)
sinSpan, cosSpan = np.sqrt(fresnel(tSpan)) #fresnelintegral erzeugen
xSpan = ((sinSpan)*Zoom)+xVerschiebung
ySpan = ((cosSpan)*Zoom)+yVerschiebung

for idx in range(len(xSpan)-1):
    x0Span, y0Span, x1Span, y1Span = xSpan[idx], ySpan[idx], xSpan[idx+1], ySpan[idx+1]
    dxSpan = x1Span-x0Span
    dySpan = y1Span-y0Span
    normSpan = math.hypot(dxSpan, dySpan) * 1/dicke
    dxSpan /= normSpan
    dySpan /= normSpan
    xcSpan = x0Span-dySpan
    ycSpan = y0Span+dxSpan
    Spandau.addPoint(xcSpan,ycSpan,0,lc,82)
    Spandau.addPoint(xcSpan,ycSpan,b,lc,83)


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

abstand = (np.sqrt(np.square(xcSpan-1)+np.square(ycSpan-2.5)))
vektorx = norm2*(abstand/4)
vektory = norm2*(abstand/4)*2.5
Spandau.addPoint(1+vektorx, 2.5+vektory,0,lc,76)
Spandau.addPoint(1+vektorx, 2.5+vektory,b,lc,77)
Spandau.addPoint((1+vektorx)-Spanx, (2.5+vektory)-Spany,0,lc,78)
Spandau.addPoint((1+vektorx)-Spanx, (2.5+vektory)-Spany,b,lc,79)

Spandau.addBSpline([70,74,78,80,1000],degree=3)
Spandau.addBSpline([71,75,79,81,3000],degree=3)
Spandau.addBSpline([1,76,82,2000],degree=3)
Spandau.addBSpline([73,77,83,4000],degree=3)

Spandau.synchronize()
gmsh.model.mesh.generate(1)
gmsh.write("Kringel.msh")
gmsh.fltk.run()
gmsh.clear()
gmsh.finalize()
