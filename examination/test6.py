from scipy.stats import binom

def nc_of_binom():
    rv = binom(10,0.2)
    print(rv.mean())
    print(rv.var())
    print(rv.moment(1))
    print(rv.moment(2))
    print(rv.moment(3))
    print(rv.moment(4))
    print(rv.stats(moments='mvsk'))

#the code should not be changed
if __name__ == '__main__':
    nc_of_binom()