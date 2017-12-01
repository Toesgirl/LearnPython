# coding=utf-8
from math import log
#计算给定数据集的香农熵：度量数据集的无序程度
def calcShannonEnt(dataSet):
    numEntries=len(dataSet)#实例的总数
    labelCounts={}#建立一个数据字典：记录这种类型的实例有多少个
    for featVec in dataSet:
        currentLabel=featVec[-1]#取出最后一个实例
        if currentLabel not in labelCounts.keys():#初始化为０
            labelCounts[currentLabel] =0
        labelCounts[currentLabel] +=1#若调用dataSet的数据，则结果为#labelCounts={[1,1,'yes']:2,
                                                                ##          [1,0,'no']:1,
                                                                  #         [0,1,'no']:2}

    shannonEnt =0.0
    for key in labelCounts:
        prob= float(labelCounts[key])/numEntries
        shannonEnt -=prob * log(prob,2)#公式h(x)=-p(x)log2[p(x)] ::注：求和
    return shannonEnt#熵越高，则混合的数据越多