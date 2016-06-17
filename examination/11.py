#-*- coding:utf-8 -*-
import sys
import numpy as np
import matplotlib.plot_api as plt
from scipy.stats import geom as G

def geom_pmf():
    rv=G(0.2)#probability of success is 0.2
    x = np.arange(1, 11, 1)#return evenly spaced values within 1 interval between [1,11)
    y = rv.pmf(x)#probability mass function
    
    plt.bar(x, y, width=0.6,  color='grey')#make bar chart
    plt.savefig('fig.png')

#the code should not be changed
if __name__ == '__main__':
    geom_pmf()