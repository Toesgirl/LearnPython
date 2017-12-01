# coding=utf-8
import calcShannonEnt
import splitDataSet
#选择最好的数据集划分方式；代码告诉你哪一个特征最好的用于划分数据集
##    dataSet =[[1,1,'yes'],
#              [1,1,'yes'],
#              [1,0,'no'],
#              [0,1,'no'],
#              [0,1,'no']]

def chooseBestFeatureToSplit(dataSet):
    numFeatures=len(dataSet[0])-1
    #前提：数据是由列表元素组成的列表，列表元素具有相同的长度；除去标签，假设有两个特征
    baseEntropy=calcShannonEnt.calcShannonEnt(dataSet)#计算出最初的无序度量度
    bestInfoGain=0.0
    bestFeature=-1
    for i in range(numFeatures):#2；ｉ代表索引值；第几个特征
        featList=[example[i] for example in dataSet]#除去标签，提取出了所有的特征
        uniqueVals=set(featList)#ｓｅｔ：每个值互不相同；除去相同的特征
        newEntropy=0.0
#以上代码创建出了唯一的分类标签列表；将数据集中所有ｉ个特征值写入新的列表中
        for value in uniqueVals:
            subDataSet=splitDataSet.splitDataSet(dataSet,i,value)#i代表第几个特征
            prob=len(subDataSet)/float(len(dataSet))
            newEntropy +=prob*calcShannonEnt.calcShannonEnt(subDataSet)
# 这个ｆｏｒ循环计算每一种划分方法的信息熵;
            infoGain=baseEntropy-newEntropy
            if (infoGain>bestInfoGain):
                bestInfoGain=infoGain
                bestFeature=i
#计算出最好的信息增益，比较所有特征中的信息增益，返回最最好特征划分的索引值
    return bestFeature