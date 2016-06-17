#-*- coding:utf-8 -*-
import sys
import numpy as np
import matplotlib.plot_api as plt
from scipy.stats import poisson as Pie

def poisson_pmf():
    rv=Pie(4.5)#the average incident is 4.5
    x = np.arange(0, 11, 1)#return evenly spaced values within 1 interval between [1,11)
    y = rv.pmf(x)#probability mass function
    
    plt.bar(x, y, width=0.6,  color='grey')#make bar chart
    plt.savefig('fig.png')

#the code should not be changed
if __name__ == '__main__':
    poisson_pmf()