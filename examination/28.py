#-*- coding:utf-8 -*-
import sys
import numpy as np
import matplotlib.plot_api as plt
from scipy.stats import bernoulli

def law_of_large_numbers():
    x = np.arange(1, 1001, 1) 
    r = bernoulli.rvs(0.3, size=1000)
    y = []
    rsum =0.0
    for i in range(1000):
        if r[i]==1:
            rsum=rsum+1
        y.append(rsum/(i+1))
    plt.plot(x, y, color='red')
    plt.savefig('law_of_large_numbers.png')

#the code should not be changed
if __name__ == '__main__':
    law_of_large_numbers()