#-*- coding:utf-8 -*-
from scipy import stats
from log_api import log

def ttest():
    x = stats.norm.rvs(loc=5, scale=10, size=50)

    log(stats.ttest_1samp(x,5.0))
    log(stats.ttest_1samp(x,1.0))

#the code should not be changed
if __name__ == '__main__':
    ttest()