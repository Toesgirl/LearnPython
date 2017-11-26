# coding=utf-8
from numpy import *
import operator
#归一化特征值，newvalue=(oldvalue-min)/(max-min)
def autoNorm(dataSet):
    minVals=dataSet.min(0)#每一类的最小值，０代表从参数列中选取最小值
    maxVals=dataSet.max(0)
    ranges=maxVals-minVals
    #公式的除数部分
    normDataSet=zeros(shape(dataSet))#建立一个与dataset维数相同的０矩阵，ｓｈａｐｅ的算出这个矩阵的行列
    m=dataSet.shape[0]#多少行
    normDataSet=dataSet-tile(minVals,(m,1))#tile将变量复制成ｍ行，１列的ｍｉｎｖａｌｓ矩阵的矩阵
    #公式的除数部分
    normDataSet = normDataSet / tile(ranges, (m, 1))
    return normDataSet,ranges,minVals


