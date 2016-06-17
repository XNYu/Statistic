#-*- coding:utf-8 -*-
import sys
import numpy as np
from scipy.stats import norm
import matplotlib.plot_api as plt

def sampling_distribution():
    fig, ax = plt.subplots(1, 1)
    #display the probability density function
    x = np.linspace(-4, 4, 100)
    ax.plot(x, norm.pdf(x))

    #simulate the sampling distribution
    y = []
    n=100
    for i in range(1000):
        r = norm.rvs(loc=5, scale=2, size=n)
        rsum=np.sum(r)
        z=(rsum-n*5)/np.sqrt(n*4)
        y.append(z)

    ax.hist(y, normed=True, alpha=0.2)
    plt.savefig('sampling_distribution.png')

#the code should not be changed
if __name__ == '__main__':
    sampling_distribution()