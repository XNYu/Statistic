#-*- coding:utf-8 -*-
from scipy.stats import uniform
from log_api import log

def nc_of_uniform():
    rv = uniform(loc=2, scale=6)
    log(rv.mean())
    log(rv.var())
    log(rv.moment(1))
    log(rv.moment(2))
    log(rv.moment(3))
    log(rv.moment(4))
    log(rv.stats(moments='mvsk'))

#the code should not be changed
if __name__ == '__main__':
    nc_of_uniform()