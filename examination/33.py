#-*- coding:utf-8 -*-
import sys
import numpy as np
from scipy.stats import norm
from scipy.stats import chi2
from scipy.stats import t
import matplotlib.plot_api as plt

def t_distribution():
    fig, ax = plt.subplots(1, 1)
    #display the probability density function
    df = 10
    x=np.linspace(-4, 4, 100)
    ax.plot(x, t.pdf(x,df))
    
    #simulate the t-distribution
    y = []
    for i in range(1000):
        rx = norm.rvs()
        ry = chi2.rvs(df)
        rt = rx/np.sqrt(ry/df)
        y.append(rt)

    ax.hist(y, normed=True, alpha=0.2)
    plt.savefig('t_distribution.png')

#the code should not be changed
if __name__ == '__main__':
    t_distribution()