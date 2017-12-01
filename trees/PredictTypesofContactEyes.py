# coding=utf-8
#使用决策树预测隐形眼睛类型
import createTree
import treePlotter
fr = open('lenses.txt')
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
lensesLabels = ['age', 'prescript' ,'aastigmatic', 'tearRate']
lensesTree = createTree.createTree(lenses, lensesLabels)
print(lensesTree)
print(treePlotter.createPlot(lensesTree))
