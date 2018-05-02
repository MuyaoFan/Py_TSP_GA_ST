import numpy as np
import collections as cl
import matplotlib
import matplotlib.pyplot as plt
def main():

    orderListArray=np.load('neworderlist3arry.npy')
    print(orderListArray.shape)
    edgeListArray=OrdertoEdge(orderListArray)
    #print(edgeListArray)
    frequenceMatrix=np.zeros((1000,1000))
    for i in edgeListArray:
        #print(i)
        for j in i:
            #print(j)
            frequenceMatrix[j[0]][j[1]] += 1
    # print(frequenceMatrix)
    # print(np.sum(frequenceMatrix))
    # print(np.max(frequenceMatrix))
    # print(frequenceMatrix[np.nonzero(frequenceMatrix)])
    print(len(frequenceMatrix[np.nonzero(frequenceMatrix)]))
    frequenceList=[]
    pointlistarray=np.transpose(np.nonzero(frequenceMatrix))
    frequencelistarray=frequenceMatrix[np.nonzero(frequenceMatrix)]
    for i in range(len(frequenceMatrix[np.nonzero(frequenceMatrix)])):

        frequencetuple=(pointlistarray[i][0],pointlistarray[i][1],frequencelistarray[i])
        frequenceList.append(frequencetuple)
    dtype=[('startpoint',int),('endpoint',int),('frequence',int)]
    frequencePointArray=np.array(frequenceList,dtype=dtype)
    frequencePointArray=np.sort(frequencePointArray,order='frequence')
    print('frequencePointArray:')
    print(frequencePointArray)
    # print(list(frequencePointArray['frequence']))
    # print(cl.Counter(frequencePointArray['frequence']))
    fPA=cl.Counter(frequencePointArray['frequence'])
    Frequenceplot(fPA)
    PlotOfEdge(frequencePointArray)
    return
def PlotOfEdge(frequencePA):

    dMatrix = np.load('distanceMatrix.npy')
    pListArray = np.load('pointListarray.npy')




    return
def Frequenceplot(fPA):
    # xticks = ['A', 'B', 'C', 'D', 'E']  # 每个柱的下标说明
    # gradeGroup = {'A': 200, 'B': 250, 'C': 330, 'D': 400, 'E': 500}  # 用于画图的频率数据

    # 创建柱状图
    # 第一个参数为柱的横坐标
    # 第二个参数为柱的高度
    # 参数align为柱的对齐方式，以第一个参数为参考标准
    plt.bar(range(1,101), [fPA.get(i, 0) for i in range(1,101)], align='center', yerr=0.000001)

    # 设置柱的文字说明
    # 第一个参数为文字说明的横坐标
    # 第二个参数为文字说明的内容
    plt.xticks(range(1,101,5), range(1,101,5))

    # 设置横坐标的文字说明
    plt.xlabel('Grade')
    # 设置纵坐标的文字说明
    plt.ylabel('Frequency')
    # 设置标题
    plt.title('Frequence of edge')
    # 绘图
    plt.show()

    return


def OrdertoEdge(oarray):
    earray=np.zeros((oarray.shape[0],oarray.shape[1]-1,2))
    for j in range(oarray.shape[0]):
        orderList=oarray[j]
        for i in range(len(orderList)-1):
            earray[j][i]=[orderList[i],orderList[i+1]]

    earray=np.sort(earray)
    earray=earray.astype(np.int32)
    #print(earray)

    return earray
main()