# coding=utf-8
#将文本记录转换为ｎｕｍｐｙ的解析程序
from numpy import *

def file2matrix(filename):
    fr=open(filename)#打开文件
    array0Lines=fr.readlines()#读取所有文件内容
    number0fLines=len(array0Lines)#得到文件行数
    returnMat=zeros((number0fLines,3))#创建返回一个number0fLines行，３列的ｎｕｍｐｙ矩阵
##以下代码是解析文件数据到列表
    classLabelVector=[]
    index=0
    for line in array0Lines:
        line=line.strip()#截掉回车符
        listFromLine=line.split('\t')#将上一步得到的整行数据分割成一个元素列表
        returnMat[index,:]=listFromLine[0:3]#将前三个元素，存储到每一行的特征矩阵中
        classLabelVector.append(int(listFromLine[-1]))#存储最后一列元素
        index +=1
    return returnMat,classLabelVector