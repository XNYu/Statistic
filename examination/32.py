#-*- coding:utf-8 -*-
import sys
import numpy as np
from scipy.stats import norm
from scipy.stats import chi2
import matplotlib.plot_api as plt

def chi2_distribution():
    fig, ax = plt.subplots(1, 1)
    #display the probability density function
    df = 10
    x=np.linspace(chi2.ppf(0.01, df), chi2.ppf(0.99, df), 100)
    ax.plot(x, chi2.pdf(x,df))
    
    #simulate the chi2 distribution
    y = []
    n=10
    for i in range(1000):
        chi2r=0.0
        r = norm.rvs(size=n)
        for j in range(n):
            chi2r=chi2r+r[j]**2
        y.append(chi2r)

    ax.hist(y, normed=True, alpha=0.2) 
    plt.savefig('chi2_distribution.png')

#the code should not be changed
if __name__ == '__main__':
    chi2_distribution()