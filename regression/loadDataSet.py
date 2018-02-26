# coding=utf-8
from numpy import *
#两种方式找出最佳拟合直线
def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split('\t')) - 1
    dataMat = []; labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat,labelMat
#标准回归函数
def standRegres(xArr,yArr):
    xMat = mat(xArr); yMat = mat(yArr).T
    xTx = xMat.T*xMat
    if linalg.det(xTx) == 0.0:#计算行向量
        print("This matrix is singular, cannot do inverse")
        return
    ws = xTx.I * (xMat.T*yMat)#回归系数
    return ws

xArr,yArr = loadDataSet('ex0.txt')
#xMat=mat(xArr)
#ws = standRegres(xArr,yArr)
#xMat = mat(xArr)
#yMat = mat(yArr)
#yHat = xMat*ws#预测出来的y值

#以下是画图
#import matplotlib.pyplot as plt
#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.scatter(xMat[:,1].flatten().A[0],yMat.T[:,0].flatten().A[0])
#xCopy=xMat.copy()
#xCopy.sort(0)#按行排序
#yHat=xCopy*ws
#ax.plot(xCopy[:,1],yHat)
#plt.show()

#yHat = xMat*ws
#print(corrcoef(yHat.T,yMat))#拟合程度，计算相关系数

#局部加权线性回归函数
def lwlr(testPoint,xArr,yArr,k=1.0):#单个数据点
    xMat = mat(xArr); yMat = mat(yArr).T
    m = shape(xMat)[0]
    weights = mat(eye((m)))#创建对角矩阵
    for j in range(m):
        diffMat = testPoint - xMat[j,:]
        weights[j,j] = exp(diffMat*diffMat.T/(-2.0*k**2))#权重值大小以指数级衰减
    xTx = xMat.T * (weights * xMat)
    if linalg.det(xTx) == 0.0:
        print("This matrix is singular, cannot do inverse")
        return
    ws = xTx.I * (xMat.T * (weights * yMat))
    return testPoint*ws
def lwlrTest(testArr,xArr,yArr,k=1.0):#数据集
    m = shape(testArr)[0]
    yHat = zeros(m)
    for i in range(m):
        yHat[i] = lwlr(testArr[i],xArr,yArr,k)
    return yHat
#print(lwlr(xArr[0],xArr,yArr,1.0))
#yHat = lwlrTest(xArr,xArr,yArr,0.01)
#xMat=mat(xArr)
#srtInd = xMat[:,1].argsort(0)#排序，输出索引值
#xSort = xMat[srtInd][:,0,:]
#import matplotlib.pyplot as plt
#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.plot(xSort[:,1],yHat[srtInd])
#ax.scatter(xMat[:,1].flatten().A[0],mat(yArr).T.flatten().A[0],s=2,c='red')
#plt.show()

#预测鲍鱼年龄
def rssError(yArr,yHatArr):
    return((yArr - yHatArr)**2).sum()
#abx,aby = loadDataSet('abalone.txt')
#yHat01 = lwlrTest(abx[0:99],abx[0:99],aby[0:99],0.1)
#yHat1 = lwlrTest(abx[0:99],abx[0:99],aby[0:99],1)
#yHat10 = lwlrTest(abx[0:99],abx[0:99],aby[0:99],10)
#print(rssError(aby[0:99],yHat01.T))
#print(rssError(aby[0:99],yHat1.T))
#print(rssError(aby[0:99],yHat10.T))
##
##-------------------------------------------------------------
##
#岭回归
def ridgeRedres(xMat, yMat, lam=0.2):
    xTx = xMat.T*xMat
    demon = xTx + eye(shape(xMat)[1])*lam
    if linalg.det(demon) == 0.0:
        print("This matrix is singular, cannot do inverse")
        return
    ws = demon.I * (xMat.T*yMat)
    return ws
def ridgeTest(xArr, yArr):
    xMat = mat(xArr); yMat = mat(yArr).T
    yMean = mean(yMat,0)
    yMat = yMat - yMean
    xMeans = mean(xMat,0)
    xVar = var(xMat,0)
    xMat = (xMat - xMeans)/xVar
    numTestPts = 30
    wMat = zeros((numTestPts,shape(xMat)[1]))
    for i in range(numTestPts):
        ws = ridgeRedres(xMat, yMat, exp(i-10))
        wMat[i,:]=ws.T
    return wMat
abx,aby = loadDataSet('abalone.txt')
#ridgeWeights=ridgeTest(abx,aby)
#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.plot(ridgeWeights)
#plt.show()
#前向逐步回归
def regularize(xMat):  # regularize by columns
    inMat = xMat.copy()
    inMeans = mean(inMat, 0)  # calc mean then subtract it off
    inVar = var(inMat, 0)  # calc variance of Xi then divide by it
    inMat = (inMat - inMeans) / inVar
    return inMat
def stageWise(xArr, yArr, eps=0.01, numIt=100):
    xMat = mat(xArr);
    yMat = mat(yArr).T
    yMean = mean(yMat, 0)
    yMat = yMat - yMean  # can also regularize ys but will get smaller coef
    xMat = regularize(xMat)
    m, n = shape(xMat)
    returnMat = zeros((numIt, n))  # testing code remove
    ws = zeros((n, 1));
    wsTest = ws.copy();
    wsMax = ws.copy()
    for i in range(numIt):  # could change this to while loop
        # print ws.T
        lowestError = inf;
        for j in range(n):
            for sign in [-1, 1]:
                wsTest = ws.copy()
                wsTest[j] += eps * sign
                yTest = xMat * wsTest
                rssE = rssError(yMat.A, yTest.A)
                if rssE < lowestError:
                    lowestError = rssE
                    wsMax = wsTest
        ws = wsMax.copy()
        returnMat[i, :] = ws.T
    return returnMat
print(stageWise(abx,aby,0.01,200))
