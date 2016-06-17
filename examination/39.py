#-*- coding:utf-8 -*-
import sys
import numpy as np
from scipy.stats import f
from scipy.stats import norm
import matplotlib.plot_api as plt

def sampling_distribution():
    fig, ax = plt.subplots(1, 1)
    #display the probability density function
    dfn, dfm = 10, 5
    x=np.linspace(f.ppf(0.01, dfn, dfm), f.ppf(0.99, dfn, dfm), 100)
    ax.plot(x, f.pdf(x, dfn, dfm))
    
    #simulate the sampling distribution
    y = []
    for i in range(1000):
        r1 = norm.rvs(loc=5, scale=2, size=dfn+1)
        r2 = norm.rvs(loc=3, scale=2, size=dfm+1)
        rf =np.var(r1)/np.var(r2)
        y.append(rf)

    ax.hist(y, normed=True, alpha=0.2)
    plt.savefig('sampling_distribution.png')

#the code should not be changed
if __name__ == '__main__':
    sampling_distribution()