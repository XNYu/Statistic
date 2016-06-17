#-*- coding:utf-8 -*-
from scipy.stats import norm
from log_api import log

def nc_of_norm():
    f1 = lambda x: x**4
    f2 = lambda x: x**2-x+2

    log(norm.expect(f1, loc=1, scale=2))
    log(norm.expect(f2, loc=2, scale=5))

#the code should not be changed
if __name__ == '__main__':
    nc_of_norm()