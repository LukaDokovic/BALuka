import numpy as np
from scipy.special import fresnel
import gmsh
import sys
import math
import os
Spandau = gmsh.model.occ
gmsh.initialize()
gmsh.open('./Stroemungsgebiet_mit_Spalt.STEP')

Zoom = 70
Anzahl = 2
Start = 0.38
Ende = 0.5
xVerschiebung = -7.47
yVerschiebung = -38
t = np.linspace(Start, Ende, Anzahl+1) #erzeugt 5 Punkte (letzter Eintrag) von 0-5 (ersten zwei Einträge)
sin, cos = np.sqrt(fresnel(t)) #fresnelintegral erzeugen
x = ((sin)*Zoom)+xVerschiebung
y = ((cos)*Zoom)+yVerschiebung
z = t * 0 - 1.5 #verschiebung in z
b = z - 25 #breite
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

#Punkte
index1 = 1000 #Original Kringel
index1list=[]
index2 = 2000 #1. Normalenvektor
index2list=[]
index3 = 3000 #Projektion des Kringels
index3list=[]
index4 = 4000 #2. Normalenvektor
index4list=[]


#über jede Koordinatenpackung iterieren
for [x,y,z] in (coords[:-1]):
        Spandau.addPoint(x, y, z, lc, index1)
        index1list.append(index1)
        index1+=1
        
Spandau.addBSpline(index1list, degree=2, tag=10000) #OriginalKringel


#dem ganzen ding eine Breite geben
for [x,y,b] in (coordsb[:-1]):
        Spandau.addPoint(x, y, b, lc, index3)
        index3list.append(index3)
        index3+=1
    
Spandau.addBSpline(index3list, degree=2, tag=30000) #Projektion des Kringels

for [xc,yc,z] in coordsd:
        Spandau.addPoint(xc, yc, z, lc, index2)
        index2list.append(index2)
        index2+=1

Spandau.addBSpline(index2list, degree=2, tag=20000) #1.Normalenvektor

for [xc,yc,b] in coordsdb:
        Spandau.addPoint(xc, yc, b, lc, index4)
        index4list.append(index4)
        index4+=1
 
Spandau.addBSpline(index4list, degree=2, tag=40000) #2.Normalenvektor
  

#Das ende des spans verbinden
Spandau.addBSpline([index1-1,index2-1], degree=1, tag=50000) #verbindet Original mit Normale (kurz)
Spandau.addBSpline([index2-1,index4-1], degree=1, tag=50001) #verbindet Normale mit Normale (lang)
Spandau.addBSpline([index3-1,index4-1], degree=1, tag=50002) #verbindet Projektion mit Normale (kurz)
Spandau.addBSpline([index3-1,index1-1], degree=1, tag=50003) #verbindet Original mit Projektion (lang)




#Vom Span aus Rückwärts
tSpan1 = Start - 0.01
sinSpan1, cosSpan1 = np.sqrt(fresnel(tSpan1)) #fresnelintegral erzeugen
xSpan1 = ((sinSpan1)*Zoom)+xVerschiebung
ySpan1 = ((cosSpan1)*Zoom)+yVerschiebung
Spandau.addPoint(xSpan1,ySpan1,z,lc,80)
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
    Spandau.addPoint(xcSpan,ycSpan,z,lc,82)
    Spandau.addPoint(xcSpan,ycSpan,b,lc,83)


#Fester Span
Spandau.addPoint(dicke,0,z,lc,90)
Spandau.addPoint(dicke,0,b,lc,91)
Spandau.addPoint(0,0,b,lc,92)
Spandau.addPoint(1,2.5,b,lc,93)


#Anfang des Spans
Spandau.addBSpline([90,91], degree=1, tag=50004) #verbindet Original mit Projektion (lang)
Spandau.addBSpline([91,92], degree=1, tag=50005) #verbindet Projektion mit Normale (kurz)
#aufgrund der geometire hinzugefügt
Spandau.addPoint(0,0,z,lc,100)
Spandau.addBSpline([90,100], degree=1, tag=50006)#verbindet Original mit Normale (kurz)



#verbindet Normale mit Normale (lang) wird gegeben durch Linie 44 (bereits im Modell
#??? ersatz für Linie 44
Spandau.addBSpline([100,92],degree=1, tag=50009)

norm2 = 1/np.sqrt(1+np.square(2.5))
Spanx = dicke * (-2.5*norm2)
Spany = dicke * (1*norm2)
Spandau.addPoint(1-Spanx,2.5-Spany,z,lc,94)
Spandau.addPoint(1-Spanx,2.5-Spany,b,lc,95)

abstand = (np.sqrt(np.square(xcSpan-1)+np.square(ycSpan-2.5)))
vektorx = norm2*(abstand/4)
vektory = norm2*(abstand/4)*2.5
Spandau.addPoint(1+vektorx, 2.5+vektory,z,lc,96)
Spandau.addPoint(1+vektorx, 2.5+vektory,b,lc,97)
Spandau.addPoint((1+vektorx)-Spanx, (2.5+vektory)-Spany,z,lc,98)
Spandau.addPoint((1+vektorx)-Spanx, (2.5+vektory)-Spany,b,lc,99)

Spandau.addBSpline([90,94,98,80,1000], degree=3, tag=60001) #OriginalKringel
Spandau.addBSpline([91,95,99,81,3000], degree=3, tag=60002) #Projektion des Kringels
Spandau.addBSpline([12,96,82,2000], degree=3, tag=60003) #1. Nomalenvektor
Spandau.addBSpline([93,97,83,4000], degree=3, tag=60004) #2. Normalenvektor


#wegen neuer geometrie Splines am festen Span
Spandau.addBSpline([12,100], degree=1, tag=50007)
Spandau.addBSpline([11,92], degree=1, tag=50008)



"""
#Flächen

#Flächen links und rechts (dicke) des Spans
Spandau.addCurveLoop([50006,60001,10000,50000,20000,60003,50007], tag = 70001)
Spandau.addCurveLoop([50005,60002,30000,50002,40000,60004,50008], tag = 70002)
Spandau.addPlaneSurface([70001], 100001)
Spandau.addPlaneSurface([70002], 100002)


#Flächen an Anfang und Ende des Spans
Spandau.addCurveLoop([50004,50006,50009,50005], tag = 80005)
Spandau.addCurveLoop([50000,50001,50002,50003], tag = 80006)
Spandau.addPlaneSurface([80005], 100005)
Spandau.addPlaneSurface([80006], 100006)

#Flächen oben und unten vom Span
Spandau.addCurveLoop([11,60003,20000,50001,40000,60004], tag = 90003)
Spandau.addCurveLoop([50004,60001,10000,50003,30000,60002], tag = 90004)
#Spandau.addSurfaceFilling(90004 , tag=100007, pointTags=[90,91,1010])
Spandau.addThruSections([70001,70002],999)

"""

Spandau.synchronize()
gmsh.model.mesh.generate(1)
gmsh.write("Kringel.msh")
gmsh.fltk.run()
gmsh.clear()
gmsh.finalize()
