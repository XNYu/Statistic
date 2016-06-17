#-*- coding:utf-8 -*-
import sys
import numpy as np
import matplotlib.plot_api as plt
from scipy.stats import binom
from scipy.stats import poisson
from scipy.stats import norm

def law_of_large_numbers():
    x = np.arange(1, 1001, 1) 
    r1 = binom.rvs(10, 0.6, size=1000)
    r2 = poisson.rvs(mu=6, size=1000)
    r3 = norm.rvs(loc=6, size=1000)

    y = []
    rsum=0.0
    for i in range(1000):
        rsum=rsum+(r1[i]+r2[i]+r3[i])
        y.append(rsum/((i+1)*3)-6)

    plt.plot(x, y, color='red')
    plt.savefig('law_of_large_numbers.png')

#the code should not be changed
if __name__ == '__main__':
    law_of_large_numbers()