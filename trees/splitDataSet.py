# coding=utf-8
# 按照给定特征划分数据集
def splitDataSet(dataSet, axis, value):
    ##           带划分的数据集　　
    ##                     数据集中每行第axis个元素
    ##                           需要返回的特征的值;即用来划分的特征
    retDataSet=[]
    for featVec in dataSet:
        if featVec[axis]==value:#每行的第axis个元素＝划分数据集的特征
            reduceFeatVce=featVec[:axis]
            reduceFeatVce.extend(featVec[axis+1:])#其他剩余的数抽取出来
            retDataSet.append(reduceFeatVce)
            # a=[1,2],b=[3,4] a.append(b):[1,2,[3,4]]
            #a.extend(b):[1,2,3,4]
    return retDataSet
