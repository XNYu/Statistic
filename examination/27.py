#-*- coding:utf-8 -*-
import numpy as np
from scipy import integrate
from scipy.stats import expon
from log_api import log

def nc_of_expon():
    #1st non-center moment of expon distribution whose lambda is 0.5
    E1 = lambda x: x*0.5*np.exp(-x/2)
    #2nd non-center moment of expon distribution whose lambda is 0.5
    E2 = lambda x: x**2*0.5*np.exp(-x/2)
    log(integrate.quad(E1, 0, np.inf))
    log(integrate.quad(E2, 0, np.inf))

    log(expon(scale=2).moment(1))
    log(expon(scale=2).moment(2))

#the code should not be changed
if __name__ == '__main__':
    nc_of_expon()