#-*- coding:utf-8 -*-
import sys
import numpy as np
from scipy.stats import binom
import matplotlib.plot_api as plt

def central_limit_theorem():
    y = []
    n=100
    for i in range(1000):
        r = binom.rvs(n, 0.3)
        rsum=np.sum(r)
        z=(rsum-n*0.3)/np.sqrt(n*0.3*0.7)
        y.append(z)
    
    plt.hist(y,color='grey')
    plt.savefig('central_limit_theorem.png')

#the code should not be changed
if __name__ == '__main__':
    central_limit_theorem()