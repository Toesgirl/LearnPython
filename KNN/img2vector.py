# coding=utf-8
from numpy import *
#将图像转化为向量，将一个３２＊３２的二进制图像矩阵转为１＊１０２４的向量
def img2vector(filename):
    returnVect=zeros((1,1024))#创建一个矩阵
    fr=open(filename)
    for i in range(32):
        lineStr=fr.readline()#读取每一行
        for j in range(32):
            returnVect[0,32*i+j]=int(lineStr[j])#将每一行放入这个向量中
    return returnVect