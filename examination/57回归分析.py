#-*- coding:utf-8 -*-
import matplotlib.plot_api as plt
import numpy as np
from scipy import stats
from log_api import log

def linregress1():
    x = np.linspace(-5, 5, num=150)
    y = x + np.random.normal(size=x.size)
    y[12:14] += 10 
    
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    log(slope)
    log(intercept)
    log(r_value)
    log(p_value)
    log(std_err)
    
    plt.plot(x, y, 'b.')
    plt.plot(x, slope * x + intercept, 'r-')
    plt.savefig('linregress1.png')
    
def linregress2():
    x = np.linspace(-5, 5, num=150)
    y = x**2 + np.random.normal(size=x.size)
    y[12:14] += 10 
    y[137:141] -= 6
    x1=x**2
    slope, intercept, r_value, p_value, std_err = stats.linregress(x1,y)
    log(slope)
    log(intercept)
    log(r_value)
    log(p_value)
    log(std_err)
    
    plt.plot(x, y, 'b.')
    plt.plot(x, slope * x1 + intercept, 'r-')
    plt.savefig('linregress2.png')

#the code should not be changed
if __name__ == '__main__':
    linregress1()
    linregress2()