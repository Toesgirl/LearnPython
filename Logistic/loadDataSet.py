# coding=utf-8
from numpy import *
import numpy as np
#用例子找出最佳的回归系数
def loadDataSet():
    dataMat = []; labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()#头为一处字符串；切片
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat

def sigmoid(inX):
    return longfloat(1.0/(1+exp(-inX)))

#梯度上升法
def gradAscent(dataMatIn, classLabels):
    dataMatrix = mat(dataMatIn)#转换为numpy矩阵数据类型
    labelMat = mat(classLabels).transpose()#转置
    m,n = shape(dataMatrix)#行列
    alpha = 0.001
    maxCycles = 500
    weights = ones((n, 1))#y=w0x0+w1x1+w2x2...梯度上升w:=w+a@f(w)
    for k in range(maxCycles):
        h = sigmoid(dataMatrix*weights)
        error = (labelMat - h)
        weights = weights + alpha * dataMatrix.transpose() * error#这里是在计算真实类别与预测类别的差值，接下来是按照差值的方向调整回归系数
    return weights
#随机梯度上升,使用样本随机选择和动态alpha动态减少机制
def stocGradAscent0(dataMatrix, classLabels, numIter=150):#迭代150次
    m,n = shape(dataMatrix)
    weights = ones(n)
    for j in range(numIter):
        dataIndex = range(m)
        for i in range(m):
            alpha = 4/(1.0+j+i)+0.01#每次减少1/(j+i)
            randIndex = int(random.uniform(0, len(dataIndex)))
            h = sigmoid(sum(dataMatrix[randIndex]*weights))
            error = classLabels[randIndex] - h
            weights = weights + alpha * error * dataMatrix[randIndex]
    return weights

#画出决策边界
def plotBestFit(weights):
    import matplotlib.pyplot as plt
    dataMat, labelMat=loadDataSet()
    dataArr = array(dataMat)
    n = shape(dataArr)[0]#取出第一个数
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    for i in range(n):
        if int(labelMat[i])==1:
            xcord1.append(dataArr[i,1]); ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i, 1]);ycord2.append(dataArr[i, 2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = arange(-3.0, 3.0, 0.1)
    y = (-weights[0]-weights[1]*x)/weights[2]
    ax.plot(x,y)
    plt.xlabel('x1'); plt.ylabel('x2')
    plt.show()
#a,b=loadDataSet()
#w=gradAscent(a,b)
#print(plotBestFit(w.getA()))#从上述结果中可以看书getA()函数与mat()函数的功能相反，是将一个numpy矩阵转换为数组
##a,b=loadDataSet()
##w=stocGradAscent0(array(a),b)
##print(plotBestFit(w))




