'''
Wilcoxon秩和检验通常用于检验成对观测数据之差是否来自均值为0的总体。下面为Wilcoxon秩和检验问题的python实现
'''
#-*- coding:utf-8 -*-
from scipy import stats

def chisquare():
    A=[16, 18, 16, 14, 12, 12]
    B=[16, 16, 16, 16, 16, 8]

    print(stats.chisquare(A))
    print(stats.chisquare(A, f_exp=B))

#the code should not be changed
if __name__ == '__main__':
    chisquare()