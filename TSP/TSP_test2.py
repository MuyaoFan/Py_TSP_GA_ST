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
    neworderlist4=neworderlist.copy()
    startgap=100
    for i in range(startSetNumber):
        startpoint=i+startgap

        sumdistance,orderlist= NearestNeighbor(pointListArray,distanceMatrix,startpoint)
        #print(sumdistance)
        print(orderlist)
        #neworderlist[i]=TwoSwap(orderlist,distanceMatrix)
        neworderlist4[i]=TripleSwap(orderlist,distanceMatrix)
    #neworderlistarray=np.array(neworderlist)
    neworderlist4array=np.array(neworderlist4)
    print(neworderlist4array)
    #np.save('neworderlistarry',neworderlistarray)
    #np.save('neworderlist3arry', neworderlist3array)
    np.save('neworderlist4arry', neworderlist4array)
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
            print(OrderDistance(odlist, dM))
            break

    #print(OrderDistance(odlist, dM))

    return odlist


def TripleSwap(orderlist, dM):
    oL=orderlist.copy()
    while True:
        oLB=oL.copy()
        dL = np.array(range(8))
        for s in range(1,2):
            #print('s=',s)
            for i1 in range(0,n-s):
                j1=i1+s
                for k1 in list(range(0,i1))+list(range(j1+1,n)):

                    i=min(i1,k1)
                    j=min(j1,max(i1,k1))
                    k=max(k1,j1)
                    edge_1_2=dM[oL[i],oL[i+1]]
                    edge_1_3=dM[oL[i],oL[j]]
                    edge_1_4=dM[oL[i],oL[j+1]]
                    edge_1_5=dM[oL[i],oL[k]]

                    edge_3_4= dM[oL[j],oL[j + 1]]
                    edge_2_4 = dM[oL[i+1],oL[j+1]]
                    edge_2_5 = dM[oL[i+1],oL[k]]
                    edge_3_5 = dM[oL[j],oL[k]]

                    edge_5_6 = dM[oL[k],oL[k + 1]]
                    edge_4_6 = dM[oL[j+1],oL[k+1]]
                    edge_3_6 = dM[oL[j],oL[k + 1]]
                    edge_2_6 = dM[oL[i+1],oL[k+1]]

                    dL[0]=edge_1_2+edge_3_4+edge_5_6
                    dL[1]=edge_1_2+edge_3_5+edge_4_6
                    dL[2]=edge_1_3+edge_2_4+edge_5_6
                    dL[3]=edge_1_3+edge_2_5+edge_4_6
                    dL[4]=edge_1_4+edge_2_5+edge_3_6
                    dL[5]=edge_1_4+edge_3_5+edge_2_6
                    dL[6]=edge_1_5+edge_2_4+edge_3_6
                    dL[7]=edge_1_5+edge_3_4+edge_2_6
                    # dL[0]=dM[oL[i],oL[i+1]]+dM[oL[j],oL[j + 1]]+dM[oL[k],oL[k + 1]]
                    # dL[1]=dM[oL[i],oL[i+1]]+dM[oL[j],oL[k]]+dM[oL[j+1],oL[k+1]]
                    # dL[2]=dM[oL[i],oL[j]]+dM[oL[i+1],oL[j+1]]+dM[oL[k],oL[k + 1]]
                    # dL[3]=dM[oL[i],oL[j]]+dM[oL[i+1],oL[k]]+dM[oL[j+1],oL[k+1]]
                    # dL[4]=dM[oL[i],oL[j+1]]+dM[oL[i+1],oL[k]]+dM[oL[j],oL[k + 1]]
                    # dL[5]=dM[oL[i],oL[j+1]]+dM[oL[j],oL[k]]+dM[oL[i+1],oL[k+1]]
                    # dL[6]=dM[oL[i],oL[k]]+dM[oL[i+1],oL[j+1]]+dM[oL[j],oL[k + 1]]
                    # dL[7]=dM[oL[i],oL[k]]+dM[oL[j],oL[j + 1]]+dM[oL[i+1],oL[k+1]]

                    maxIndex=np.argmin(dL)

                    if maxIndex==0:
                        pass
                    elif maxIndex<3:

                        if maxIndex==1:
                            od_4_5 = oL[j + 1:k + 1]
                            #print('1')
                            od_4_5.reverse()
                            oL[j+1:k+1]=od_4_5
                        elif maxIndex==2:
                            od_2_3 = oL[i + 1:j + 1]
                            #print('2')
                            od_2_3.reverse()
                            oL[i + 1:j + 1]=od_2_3
                    elif maxIndex==3:
                        od_2_3 = oL[i + 1:j + 1]
                        od_4_5 = oL[j + 1:k + 1]
                        #print('3')
                        od_4_5.reverse()
                        oL[j + 1:k + 1] = od_4_5
                        od_2_3.reverse()
                        oL[i + 1:j + 1] = od_2_3
                    elif maxIndex==4:
                        od_2_3 = oL[i + 1:j + 1]
                        od_4_5 = oL[j + 1:k + 1]
                        #print('4')
                        odn=od_4_5+od_2_3
                        oL[i+1:k+1]=odn
                    elif maxIndex==5:
                        od_2_3 = oL[i + 1:j + 1]
                        od_4_5 = oL[j + 1:k + 1]
                        #print('5')
                        od_2_3.reverse()
                        odn = od_4_5 + od_2_3
                        oL[i + 1:k + 1] = odn
                    elif maxIndex==6:
                        od_2_3 = oL[i + 1:j + 1]
                        od_4_5 = oL[j + 1:k + 1]
                        #print('6')
                        od_4_5.reverse()
                        odn = od_4_5 + od_2_3
                        oL[i + 1:k + 1] = odn
                    elif maxIndex==7:
                        od_2_3 = oL[i + 1:j + 1]
                        od_4_5 = oL[j + 1:k + 1]
                        #print('7')
                        od_4_5.reverse()
                        od_2_3.reverse()
                        odn = od_4_5 + od_2_3
                        oL[i + 1:k + 1] = odn
                    # if maxIndex!=0:
                    #     print(OrderDistance(oL, dM))
        if oLB==oL:
            oL=ReturnToZero(oL)
            print(oL)
            print(OrderDistance(oL, dM))
            break
    return oL

def TripleSwapwithTwo(orderlist, dM):
    oL=orderlist.copy()
    maxdelt=0
    for m in range(100):
        print('m=',m)
        oLB=oL.copy()
        for i in range(n-3):
            #print('i=',i)
            for j in range(i+1,n-3):
                for k in range(j+1,n-1):
                    dL=np.array(range(5))

                    # edge_1_2=dM[oL[i],oL[i+1]]
                    # edge_1_3=dM[oL[i],oL[j]]
                    # edge_1_4=dM[oL[i],oL[j+1]]
                    # edge_1_5=dM[oL[i],oL[k]]
                    #
                    # edge_3_4= dM[oL[j],oL[j + 1]]
                    # edge_2_4 = dM[oL[i+1],oL[j+1]]
                    # edge_2_5 = dM[oL[i+1],oL[k]]
                    # edge_3_5 = dM[oL[j],oL[k]]
                    #
                    # edge_5_6 = dM[oL[k],oL[k + 1]]
                    # edge_4_6 = dM[oL[j+1],oL[k+1]]
                    # edge_3_6 = dM[oL[j],oL[k + 1]]
                    # edge_2_6 = dM[oL[i+1],oL[k+1]]
                    #
                    # dL[0]=edge_1_2+edge_3_4+edge_5_6
                    # dL[1]=edge_1_2+edge_3_5+edge_4_6
                    # dL[2]=edge_1_3+edge_2_4+edge_5_6
                    # dL[3]=edge_1_3+edge_2_5+edge_4_6
                    # dL[4]=edge_1_4+edge_2_5+edge_3_6
                    # dL[5]=edge_1_4+edge_3_5+edge_2_6
                    # dL[6]=edge_1_5+edge_2_4+edge_3_6
                    # dL[7]=edge_1_5+edge_3_4+edge_2_6
                    dL[0]=dM[oL[i],oL[i+1]]+dM[oL[j],oL[j + 1]]+dM[oL[k],oL[k + 1]]
                    #dL[1]=dM[oL[i],oL[i+1]]+dM[oL[j],oL[k]]+dM[oL[j+1],oL[k+1]]
                    #dL[2]=dM[oL[i],oL[j]]+dM[oL[i+1],oL[j+1]]+dM[oL[k],oL[k + 1]]
                    dL[1]=dM[oL[i],oL[j]]+dM[oL[i+1],oL[k]]+dM[oL[j+1],oL[k+1]]
                    dL[2]=dM[oL[i],oL[j+1]]+dM[oL[i+1],oL[k]]+dM[oL[j],oL[k + 1]]
                    dL[3]=dM[oL[i],oL[j+1]]+dM[oL[j],oL[k]]+dM[oL[i+1],oL[k+1]]
                    dL[4]=dM[oL[i],oL[k]]+dM[oL[i+1],oL[j+1]]+dM[oL[j],oL[k + 1]]
                    #dL[7]=dM[oL[i],oL[k]]+dM[oL[j],oL[j + 1]]+dM[oL[i+1],oL[k+1]]

                    maxIndex=np.argmin(dL)
                    od_2_3=oL[i+1:j+1]
                    od_4_5=oL[j+1:k+1]
                    if maxIndex==0:
                        pass
                    # elif maxIndex==1:
                    #     print('1')
                    #     od_4_5.reverse()
                    #     oL[j+1:k+1]=od_4_5
                    # elif maxIndex==2:
                    #     print('2')
                    #     od_2_3.reverse()
                    #     oL[i + 1:j + 1]=od_2_3
                    elif maxIndex==1:
                        print('3')
                        od_4_5.reverse()
                        oL[j + 1:k + 1] = od_4_5
                        od_2_3.reverse()
                        oL[i + 1:j + 1] = od_2_3
                    elif maxIndex==2:
                        print('4')
                        odn=od_4_5+od_2_3
                        oL[i+1:k+1]=odn
                    elif maxIndex==3:
                        print('5')
                        od_2_3.reverse()
                        odn = od_4_5 + od_2_3
                        oL[i + 1:k + 1] = odn
                    elif maxIndex==4:
                        print('6')
                        od_4_5.reverse()
                        odn = od_4_5 + od_2_3
                        oL[i + 1:k + 1] = odn
                    # elif maxIndex==7:
                    #     print('7')
                    #     od_4_5.reverse()
                    #     od_2_3.reverse()
                    #     odn = od_4_5 + od_2_3
                    #     oL[i + 1:k + 1] = odn
                    if maxIndex!=0:
                        print(OrderDistance(oL, dM))
                        print('i=',i,'j=',j,'k=',k)

                        delt=min(j-i,k-j)
                        maxdelt=max(maxdelt,delt)
                        print('maxdelt=',maxdelt)
        if oLB==oL:
            oL=ReturnToZero(ol)
            print(OrderDistance(oL, dM))
            break
    return oL

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
