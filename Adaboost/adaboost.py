# coding=utf-8
from numpy import *
def loadSimpData():
    datMat = matrix([[1. , 2.1],
                    [2. , 1.1],
                    [1.3, 1. ],
                    [1. , 1. ],
                    [2. , 1. ]])
    classLabels = [1.0, 1.0, -1.0, -1.0, 1.0]
    return datMat,classLabels
a,b=loadSimpData()
def stumpClassify(dataMarix, dimen, threshVal, threshIneq):#特征，第几列，比较的数，大于小于
    retArray = ones((shape(dataMarix)[0],1))
    if threshIneq == 'lt':
        retArray[dataMarix[:,dimen] <= threshVal] = -1.0#满足不等式的数设置为-1，不满足的为1
    else:
        retArray[dataMarix[:, dimen] > threshVal] = -1.0
    return retArray
#单层决策树生成树
#为的是在特征值之间找一个划分点，使分类器误差最小
def bulidStump(dataArr, classLabels, D):
    dataMatrix = mat(dataArr); labelMat = mat(classLabels).T
    m,n = shape(dataMatrix)
    numSteps = 10.0; bestStump = {}; bestClassEst = mat(zeros((m,1)))
    minError = inf
    for i in range(n):
        rangeMin = dataMatrix[:,i].min();rangeMax = dataMatrix[:,i].max()
        stepSize = (rangeMax - rangeMin)/numSteps
        for j in range(-1,int(numSteps)+1):#第二次再在这些值上遍历
            for inequal in ['lt','gt']:#在小于大于之间切换
                threshVal = (rangeMin + float(j)*stepSize)
                predictedVals = \
                stumpClassify(dataMatrix,i,threshVal,inequal)
                errArr = mat(ones((m,1)))
                errArr[predictedVals == labelMat] = 0
                weightdeError = D.T*errArr#单个分类器的误差
                print("split:dim %d, thresh %.2f, thresh ineqal:%s, the weighted\
                error is %.3f" %(i,threshVal,inequal,weightdeError))
                if weightdeError <minError:#根据权重找到最小的错误率划分点
                    minError = weightdeError
                    bestClassEst = predictedVals.copy()
                    bestStump['dim'] = i#列
                    bestStump['thresh'] =threshVal#作比较的数；分类器的划分点
                    bestStump['ineq'] = inequal#大于小于
    return bestStump,minError,bestClassEst#minError；分错样本的权重之和；bestClassEst；比较之后那几个样本错了，错误的样本分类情况
#D = mat(ones((5,1))/5)
#4print(bulidStump(a,b,D))
#基于单层决策树的Adaboost训练过程
def adaBoostTrainDS(dataArr,classLabels,numIt=40):#若算法在第三次迭代过程中错误率为0，则退出迭代过程
    weakClassArr = []
    m = shape(dataArr)[0]
    D = mat(ones((m,1))/m)
    aggClassEst = mat(zeros((m,1)))
    for i in range(numIt):
        bestStump,error,classEst = bulidStump(dataArr,classLabels,D)
        print("D:",D.T)
        alpha = float(0.5*log((1.0-error)/max(error,1e-16)))#分类器的单次权重
        bestStump['alpha'] = alpha
        weakClassArr.append(bestStump)
        print("classEst:",classEst.T)
        expon = multiply(-1*alpha*mat(classLabels).T,classEst)#分对的样本权重降低，错的是正，权重升高
        D = multiply(D,exp(expon))
        D = D/D.sum()#这三步是为下一次迭代计算样本权重
        aggClassEst +=alpha*classEst#，错误累加计算；列向量，记录每个数据点的类别估计累计值。最后看正负号是否与标签一样;类似于总的分类函数
        print("aggClassEst: ",aggClassEst.T)
        aggErrors = multiply(sign(aggClassEst) != mat(classLabels).T,ones((m,1)))#化简为便签大小
        errorRate = aggErrors.sum()/m
        print("total error: ",errorRate,"\n")
        if errorRate == 0.0:break
    return weakClassArr
#print(adaBoostTrainDS(a,b,9))
##测试算法-------------------------------------------------
#Adaboost分类函数
def adaClassify(datToClass,classifierArr):
    dataMatrix = mat(datToClass)
    m = shape(dataMatrix)[0]
    aggClassEst = mat(zeros((m,1)))
    for i in range(len(classifierArr)):
        classEst = stumpClassify(dataMatrix,classifierArr[i]['dim'],\
                                 classifierArr[i]['thresh'],\
                                 classifierArr[i]['ineq'])
        aggClassEst += classifierArr[i]['alpha']*classEst#总的分类函数
        print(aggClassEst)
    return sign(aggClassEst)
#classifierArr = adaBoostTrainDS(a,b,30)#训练分类器
#print(adaClassify([[0,0],[5,5]],classifierArr))
