import numpy as np
from scipy.special import fresnel
import gmsh
import sys
import math
import os
import matplotlib.pyplot as plt
from sympy import *


#Phase 0

#toolRoomHeight = 
#toolHeight =
start = int(0)#Startpunkt des Kringels
end = int(2) #Endpunkt des Kringels
quantityCalc = int(end * 100000) #Anzahl der Punkte des Kringels
u = np.linspace(start, end, quantityCalc) #Erzeugt die gewünschte Anzahl an Punkten zwischen Start und Endpunkt (+1 da die ableitung für die Normalenvektoren und dadurch das +1. Element genutzt wird)
function = fresnel
#modification = np.sqrt
sin, cos = (function(u)) #Erzeugt das Fresnelintegral #modification(function(u))
x = sin
y = cos
plt.plot(x, y, 'red')
plt.savefig('foo.png')

#Die Kooridnaten werden in Arrays abgepackt
coordsXCalc = (x)
resultXCalc = []
for x in coordsXCalc:
    resultXCalc.append(x)
        
coordsYCalc = (y)
resultYCalc = []
for y in coordsYCalc:
    resultYCalc.append(y) 

#Löscht jeden Eintrag aus den Koordinaten-Arrays
def resetCoords (xList,yList):
    del xList[:]
    del yList[:]

#Y-Koordinatenwert nach 180°
def getYValuePi(xList, yList):
    maxX = np.amax(xList)
    xPosition = np.where(xList == np.amax(xList))
    xPositionArray = xPosition[0]
    xPositionInt = xPositionArray[0]
    yValuePi = yList[xPositionInt]
    return yValuePi
print(getYValuePi(resultXCalc, resultYCalc))

#X-Koordinatenwert nach 180°
def getXValuePi(xList, yList):
    maxX = np.amax(xList)
    xPosition = np.where(xList == np.amax(xList))
    xPositionArray = xPosition[0]
    xPositionInt = xPositionArray[0]
    xValuePi = xList[xPositionInt]
    return xValuePi
print(getXValuePi(resultXCalc, resultYCalc))

#Arrayindex für die Koordinaten bei 180°
def getIndexPi(xList, yList):
    maxX = np.amax(xList)
    xPosition = np.where(xList == np.amax(xList))
    xPositionArray = xPosition[0]
    xPositionInt = xPositionArray[0]
    return xPositionInt
print(getIndexPi(resultXCalc, resultYCalc))

#Y-Koordinatenwert nach 90°
def getYValuePiHalf(xList, yList):
    maxY = np.amax(yList)
    yPosition = np.where(yList == np.amax(yList))
    yPositionArray = yPosition[0]
    yPositionInt = yPositionArray[0]
    yValuePiHalf = yList[yPositionInt]
    return yValuePiHalf
print(getYValuePiHalf(resultXCalc,resultYCalc))

#Arrayindex für die Koordinaten bei 90°
def getYIndexPiHalf(xList, yList):
    maxY = np.amax(yList)
    yPosition = np.where(yList == np.amax(yList))
    yPositionArray = yPosition[0]
    yIndexPiHalf = yPositionArray[0]
    return yIndexPiHalf
print(getYIndexPiHalf(resultXCalc,resultYCalc))

#Arrayindex für die Koordinaten bei 270°
def getYIndex3PiHalf(xList, yList):
    maxX = np.amax(xList)
    xPosition = np.where(xList == np.amax(xList))
    xPositionArray = xPosition[0]
    xPositionInt = xPositionArray[0]
    cutList = yList[xPositionInt:]
    minPosition = np.where(cutList == np.amin(cutList))
    minPositionArray = minPosition[0]
    yIndex3PiHalf = minPositionArray[0]+xPositionInt
    return yIndex3PiHalf
print(getYIndex3PiHalf(resultXCalc,resultYCalc))

#Y-Koordinatenwert nach 270°
def getYValue3PiHalf(xList, yList):
    maxX = np.amax(xList)
    xPosition = np.where(xList == np.amax(xList))
    xPositionArray = xPosition[0]
    xPositionInt = xPositionArray[0]
    cutList = yList[xPositionInt:]
    yValue3PiHalf = np.amin(cutList)
    return yValue3PiHalf
print(getYValue3PiHalf(resultXCalc,resultYCalc))















#toolRoomHeight = 
#toolHeight =
time = 0
start = 0.38 #Startpunkt des Kringels
end = 3 #Endpunkt des Kringels
zoom = 70 #Größe des Kringels
quantity = 50 #Anzahl der Punkte des Kringels
#quatityCalc =
xShift = -7.47 #Verschiebung in X-Richtung
yShift = -38 #Verschiebung in Y-Richtung
zShift = 0 #Verschiebung in Z-Richtung
wide = 12 #Breite des Spans
thick = 1 #Dicke des Spans
lc = -5.0 #Netzdichte an den Punkten des Kringels


u = np.linspace(start, end, quantity+1) #Erzeugt die gewünschte Anzahl an Punkten zwischen Start und Endpunkt (+1 da die ableitung für die Normalenvektoren und dadurch das +1. Element genutzt wird)
function = fresnel
modification = np.sqrt
sin, cos = modification(function(u)) #Erzeugt das Fresnelintegral
x = ((sin)*zoom) + xShift
y = ((cos)*zoom) + yShift
z = u * 0 + zShift #Lage der Symmatrieachse
b = z + wide #Breite des Kringels
    
    
    
    
    
#phase1
#phase2
#phase3
#phase4 
