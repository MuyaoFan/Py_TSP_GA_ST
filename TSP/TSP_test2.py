import numpy as np
import matplotlib.pyplot as plt

import random as rd

global n
n=1000

def main():
    distanceMatrix=np.load('distanceMatrix.npy')
    pointListArray=np.load('pointListarray.npy')
    #print(distanceMatrix)
    #print(pointListArray)
    startSetNumber=100
    neworderlist=list(range(startSetNumber))
    startgap=100
    for i in range(startSetNumber):
        startpoint=i+startgap

        sumdistance,orderlist= NearestNeighbor(pointListArray,distanceMatrix,startpoint)
        #print(sumdistance)
        print(orderlist)
        neworderlist[i]=TwoSwap(orderlist,distanceMatrix)
    neworderlistarray=np.array(neworderlist)
    print(neworderlistarray)
    np.save('neworderlistarry',neworderlistarray)
    '''
    for i in range(10):

        randomlist=TwoSwap(FixStartpointRandomList(n),distanceMatrix)
    '''
    return

def NearestNeighbor(pL,dM,startpoint):
    dm=dM.copy()
    #startpoint=4
    orderlist=[startpoint]
    sumdistance=0
    dm[ : ,startpoint]=np.ones(n)*1000
    npindex=startpoint

    for i in range(n-1):
        tempA1=dm[npindex]
        distance=tempA1.min()
        npindexarray=np.where(tempA1==distance)
        npindex=npindexarray[0][0]
      #  print(npindex)
        orderlist.append(npindex)
        sumdistance += distance
        dm[ : ,npindex]=np.ones((n))*1000
    orderlist.append(startpoint)
    sumdistance=sumdistance+dM[npindex][startpoint]
    return sumdistance,orderlist

def TwoSwap(orderlist,dM):
    odlist=orderlist.copy()

    #oldlist=odlist.copy()
    for k in range(10):
        odlistbackup=odlist.copy()
        for i in range(1,n-2):
            #print('i=',i)
            for j in range(n-i-1):
                #print('j=',j)
                if (dM[odlist[j]][odlist[j+1]]+dM[odlist[j+1+i]][odlist[j+2+i]]) >= (dM[odlist[j]][odlist[j+1+i]]+dM[odlist[j+1]][odlist[j+2+i]]):
                    piece = odlist[j + 1:j + 2 + i]
                    piece.reverse()
                    odlist[j + 1:j + i + 2] = piece

        if odlistbackup==odlist:
            odlist=ReturnToZero(odlist)
            #print('break')
            #print(odlist)
            break

    #print(OrderDistance(odlist, dM))

    return odlist

def OrderDistance(odlist,dM):
    sumdistance=0
    for i in range(n-1):
        sumdistance=sumdistance+dM[odlist[i]][odlist[i+1]]

    return sumdistance

def FixStartpointRandomList(n):
    randomlist=list(range(1,n))
    rd.shuffle(randomlist)
    randomlistnew=[0]+randomlist+[0]
    return randomlistnew

def ReturnToZero(orderlist):
    list1=orderlist.copy()

    list1.pop()
    list2 =list1[:list1.index(0)]
    list3 =list1[list1.index(0):]
    list1=list3+list2
    list1.append(0)
    return list1

main()
