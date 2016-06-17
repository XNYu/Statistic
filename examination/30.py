#-*- coding:utf-8 -*-
import sys
import numpy as np
from scipy.stats import expon
import matplotlib.plot_api as plt

def central_limit_theorem():
    y = []
    n=100
    for i in range(1000):
        r = expon.rvs(scale=1, size=n)
        rsum=np.sum(r)
        z=(rsum-n)/np.sqrt(n)
        y.append(z)
    
    plt.hist(y,color='grey')
    plt.savefig('central_limit_theorem.png')

#the code should not be changed
if __name__ == '__main__':
    central_limit_theorem()