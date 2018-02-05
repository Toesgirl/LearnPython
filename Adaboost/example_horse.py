# coding=utf-8
from numpy import *
import adaboost
def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split('\t'))
    dataMat = []; labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat-1):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat,labelMat
datArr,labelArr=loadDataSet('horseColicTraining2.txt')
classifierArray = adaboost.adaBoostTrainDS(datArr,labelArr,10)
print(classifierArray)
testArr,testLabelArr = loadDataSet('horseColicTest2.txt')
prediction10 = adaboost.adaClassify(testArr,classifierArray)
errArr = mat(ones((67,1)))
a=errArr[prediction10 != mat(testLabelArr).T].sum()
print(a)
