# coding=utf-8
# xy设置箭头尖的坐标
# xytext设置注释内容显示的起始位置
# arrowprops 用来设置箭头
# 可以通过设置xy和xytext中坐标的值来设置箭身是否倾斜
import matplotlib.pyplot as plt
#定义文本框和箭头格式
decisionNode=dict(boxstyle="sawtooth",fc="0.8")#决策节点,boxstyle:锯齿fc控制的注解框内的颜色深度
leafNode=dict(boxstyle="round4",fc="0.8")#叶子节点　　　　　
arrow_args=dict(arrowstyle="<-")#箭头格式
#绘制带箭头的格式
#nodeTxt：节点的文字标注, centerPt：节点中心位置,
#parentPt：箭头起点位置（上一节点位置）, nodeType：节点属性 , xytext:注解框位置
def plotNode(nodeTxt,centerPt,parentPt,nodeType):
    createPlot.ax1.annotate(nodeTxt,xy=parentPt,xycoords='axes fraction',\
                            xytext=centerPt,textcoords='axes fraction',\
                            va="center",ha="center",bbox=nodeType,arrowprops=arrow_args)
# coding=utf-8.............................................................................
#获取叶子节点的数目和树的层数
#必须知道有多少个叶子节点，来确定x轴的长度
def getNumLeafs(myTree):#{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}
    numLeafs=0
    firstStr=myTree.keys()[0]#'no surfacing'
    secondDict=myTree[firstStr]#0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':#是否是字典
            numLeafs+=getNumLeafs(secondDict[key])
        else:    numLeafs +=1#如果是叶节点，则叶节点+1
    return numLeafs
#还需要知道树有多少层，以便确定y轴的高度
def getTreeDepth(myTree):
    maxDepth=0
    firstStr=myTree.keys()[0]
    secondDict=myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':
            thisDepth=1+getTreeDepth(secondDict[key])#如果是字典，则层数加1，再递归调用
        else:    thisDepth=1
        if thisDepth>maxDepth: maxDepth = thisDepth#得到最大层数
    return maxDepth
# coding=utf-8......................................................................
#在父子节点间填充文本信息
#cntrPt:子节点位置, parentPt：父节点位置, txtString：标注内容
def plotMidText(cntrPt, parentPt, txtString):
    xMid=(parentPt[0]-cntrPt[0])/2.0+cntrPt[0]
    yMid=(parentPt[1]-cntrPt[1])/2.0+cntrPt[1]
    createPlot.ax1.text(xMid,yMid,txtString)
# coding=utf-8..........................................................................
#绘制树形图
#myTree：树的字典, parentPt:父节点, nodeTxt：节点的文字标注
def plotTree(myTree, parentPt, nodeTxt):
    numLeafs = getNumLeafs(myTree)
    depth = getTreeDepth(myTree)
    firstStr = myTree.keys()[0]
    # 计算当前节点的位置
    cntrPt = (plotTree.x0ff + (1.0 + float(numLeafs))/2.0/plotTree.totalW,plotTree.y0ff)
    plotMidText(cntrPt, parentPt, nodeTxt)#在父子节点间填充文本信息
    plotNode(firstStr, cntrPt, parentPt, decisionNode)#绘制带箭头的注解
    secondDict = myTree[firstStr]
    plotTree.y0ff = plotTree.y0ff - 1.0/plotTree.totalD#减少y偏差
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':
            plotTree(secondDict[key],cntrPt,str(key))#递归绘制树形图
        else:#如果是叶节点
            plotTree.x0ff=plotTree.x0ff + 1.0/plotTree.totalW
            plotNode(secondDict[key], (plotTree.x0ff, plotTree.y0ff), cntrPt, leafNode)
            plotMidText((plotTree.x0ff, plotTree.y0ff), cntrPt, str(key))
    plotTree.y0ff = plotTree.y0ff + 1.0/plotTree.totalD#递减y坐标值
# coding=utf-8............................................................................
#创建绘图区
def createPlot(inTree):
    fig = plt.figure(1,facecolor='white')#背景颜色是白色
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)
    plotTree.totalW = float(getNumLeafs(inTree))#全局变量plotTree.totalW，plotTree.totalD用来计算树节点的摆放位置
    plotTree.totalD = float(getTreeDepth(inTree))
    plotTree.x0ff = -0.5/plotTree.totalW#全局变量plotTree.x0ff,plotTree.y0ff用来存储已绘制的节点位置，以及放置下一个节点的位置
    plotTree.y0ff =1.0
    plotTree(inTree, (0.5,1.0), '')
    plt.show()


a={'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}
print(createPlot(a))
