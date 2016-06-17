#-*- coding:utf-8 -*-
import sys
import numpy as np
import matplotlib.plot_api as plt
from scipy.stats import expon as E

def expon_pdf():
    x = np.linspace(0, 20, 100)#return evenly spaced samples, calculated over the interval [0,20]
    rv1=E(scale = 1.5)#the scale is 1.5
    rv2=E(scale = 1.0)#the scale is 1.0
    rv3=E(scale = 0.5)#the scale is 0.5

    plt.plot(x, rv1.pdf(x), color='green')#make chart
    plt.plot(x, rv2.pdf(x), color='blue')#make chart
    plt.plot(x, rv3.pdf(x), color='red')#make chart
    plt.savefig('fig.png')

#the code should not be changed
if __name__ == '__main__':
    expon_pdf()