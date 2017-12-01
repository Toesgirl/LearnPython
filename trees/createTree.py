# coding=utf-8
import majorityCnt
import chooseBestFeatureToSplit
import splitDataSet
import createDataSet
#创建树的函数代码，递归方式

def createTree(dataSet,labels):#输入数据集和标签列表
    classList=[example[-1] for example in dataSet]#取出数据集的最后一列：即这个样本的类别，分类结果
    if classList.count(classList[0])==len(classList):#ｃｏｕｎｔ用来计数
        return classList[0]
#第一个停止条件：类别完全相同则灵芝划分
    if len(dataSet[0])==1:
        return majorityCnt.majorityCnt(classList)
#　第二个停止条件：遍历完所有特征是返回出现次数最多的
    bestFeat=chooseBestFeatureToSplit.chooseBestFeatureToSplit(dataSet)#最优的划分特征，返回的是索引值
    bestFeatLabel=labels[bestFeat]#取出对应的标签

    myTree={bestFeatLabel:{}}
    del(labels[bestFeat])#删除

    featValues=[example[bestFeat] for example in dataSet]#取出列表包含的所有特征值
    uniqueVals=set(featValues)
    for value in uniqueVals:
        subLabels=labels[:]
        #创建新的标签列表
        myTree[bestFeatLabel][value]=createTree(splitDataSet.splitDataSet(dataSet,bestFeat,value),subLabels)
    return myTree


