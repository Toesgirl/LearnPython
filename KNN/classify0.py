# coding=utf-8
from numpy import *
import operator
def classify0(inX,dataSet,labels,k):#定义了四个输入参数
    dataSetSize=dataSet.shape[0]#shape:矩阵的行数；训练样本的个数
    diffMat=tile(inX,(dataSetSize,1))-dataSet#tile:重复某个数组；ｘa0-xb0
    sqDiffMat=diffMat**2#(xa0-xb0)**2
    sqDistances=sqDiffMat.sum(axis=1)#axis:按行数相加
    distances=sqDistances**0.5
    sortedDistIndicies=distances.argsort()#ardsort:从小到大排序，返回的是*索引值*
#以上代码是计算已知类别数据集中的点与当前点之间的距离，并且按照距离从小到大排序，返回值是每个值得序号
    classCount={}#定义一个空的ｄｉｃｔ
    for i in range(k):
        voteIlabel=labels[sortedDistIndicies[i]]
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
        #取出ｋ个点的属性值（ｌａｂｅｌs），并统计属性的个数
#以上是选择距离最小的ｋ个点，确定个点频率
    sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
                                       #iteritems:迭代器，分解成元祖列表
##　　　　　　　　　　　　　　　　　　　                       #operator.itemgetter:选择第２个元素排序
    return sortedClassCount[0][0]#返回频率最高的类别作为当前点的预测分类
