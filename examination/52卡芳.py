# 卡方拟合优度检验通常用于根据样本的频数分布来推断总体的分布。下面为卡方拟合优度检验问题的python实现，请完成以下练习：
#-*- coding:utf-8 -*-
from scipy import stats
from log_api import log

def chisquare():
    A=[16, 18, 16, 14, 12, 12]
    B=[16, 16, 16, 16, 16, 8]

    log(stats.chisquare(A))
    log(stats.chisquare(A, f_exp=B))

#the code should not be changed
if __name__ == '__main__':
    chisquare()