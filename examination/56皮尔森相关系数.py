'''
皮尔森相关系数用于度量两个变量之间相关程度，介于-1到1之间，其中-1表示完全负相关，0表示无关，1表示完全正相关。
'''
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def pearsonr():
    x = np.linspace(-5, 5, num=150)
    y = x + np.random.normal(size=x.size)
    y[12:14] += 10
    
    print(stats.pearsonr(x, y))
    plt.scatter(x,y)
    plt.savefig('pearsonr.png')
    plt.show()
#the code should not be changed
if __name__ == '__main__':
    pearsonr()