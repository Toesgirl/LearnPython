# coding=utf-8
from numpy import *
import operator
import file2matrix
import autoNorm
import classify0
##使用算法：约会网站预测函数
def classifyPerson():
    resultList=['not at all','in small doses','in large doses']#三种标签组成一个向量
    percentTats=float(raw_input("percentage of time spent playing video games?"))
    ffMiles=float(raw_input("frequent filer miles earned per years?"))
    iceCream=float(raw_input("liters of ice cream consumed per year?"))##用raw_input函数输入三个文本行命令
    datingDataMat,datingLabels=file2matrix.file2matrix('datingTestSet2.txt')
    normMat,ranges,minVals=autoNorm.autoNorm(datingDataMat)##对已知的样本格式处理
    inArr=array([ffMiles,percentTats,iceCream])#输入的三个参数组成一个向量
    classifierResult=classify0.classify0((inArr-minVals)/ranges,normMat,datingLabels,3)
    ##                                      对输入的三个参数归一化数值
    print("You will probably like this person: ", resultList[classifierResult-1])
