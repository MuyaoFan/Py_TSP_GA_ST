# -*- coding: utf-8 -*-
import random as rd
import numpy as np
from math import sqrt

global n                      # The number of notions
n= 1000


def main():
    pointListarray,distanceMatrix=GraphGenerate(n)
  #  print(distanceMatrix)
    print (distanceMatrix)
    print (pointListarray)
    np.save('distanceMatrix',distanceMatrix)
    np.save('pointListarray',pointListarray)

def GraphGenerate(n):
    pointList=[]
    for i in range(n):
        x=rd.uniform(-100,100)
        y=rd.uniform(-100,100)
        point=[x,y,i]
        pointList.append(point)
    pointListarray=np.array(pointList)
    distanceMatrix=np.zeros((n,n))
    
    print(distanceMatrix)

    for i in range(n):
        for j in range(n):
            if i==j:
                distanceMatrix[i][j]=1000
            else:
                distanceMatrix[i][j]=Distance(pointList[i],pointList[j])
    return pointListarray,distanceMatrix

def Distance(a,b):
    distance=sqrt((a[0]-b[0])*(a[0]-b[0])+(a[1]-b[1])*(a[1]-b[1]))
    return distance



main()
