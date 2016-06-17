#-*- coding:utf-8 -*-
import sys
import numpy as np
from scipy.stats import t
from scipy.stats import norm
import matplotlib.plot_api as plt

def sampling_distribution():
    fig, ax = plt.subplots(1, 1)
    #display the probability density function
    df = 10
    x=np.linspace(t.ppf(0.01, df), t.ppf(0.99, df), 100)
    ax.plot(x, t.pdf(x, df))
    
    #simulate the sampling distribution
    y = []
    for i in range(1000):
        r = norm.rvs(loc=5, scale=2, size=df+1)
        rt =(np.mean(r)-5)/np.sqrt(np.var(r)/df)
        y.append(rt)

    ax.hist(y, normed=True, alpha=0.2)
    plt.savefig('sampling_distribution.png')

#the code should not be changed
if __name__ == '__main__':
    sampling_distribution()