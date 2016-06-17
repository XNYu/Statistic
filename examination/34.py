#-*- coding:utf-8 -*-
import sys
import numpy as np
from scipy.stats import norm
from scipy.stats import chi2
from scipy.stats import f
import matplotlib.plot_api as plt

def F_distribution():
    fig, ax = plt.subplots(1, 1)
    #display the probability density function
    dfn, dfm = 10, 5
    x = np.linspace(f.ppf(0.01, dfn, dfm), f.ppf(0.99, dfn, dfm), 100)
    ax.plot(x, f.pdf(x, dfn, dfm))
    
    #simulate the F-distribution
    y = []
    for i in range(1000):
        rx = chi2.rvs(dfn)
        ry = chi2.rvs(dfm)
        rf = np.sqrt(rx/dfn)/np.sqrt(ry/dfm)
        y.append(rf)

    ax.hist(y, normed=True, alpha=0.2)
    plt.savefig('F_distribution.png')

#the code should not be changed
if __name__ == '__main__':
    F_distribution()