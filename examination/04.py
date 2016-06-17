#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.plot_api as plt

def get_data():
    # example data
    mu = 100 # mean of distribution
    sigma = 15 # standard deviation of distribution
    x = mu + sigma * np.random.randn(8)
    return x

#you can write your code here
def draw():
    #get input data
    x = get_data()
    c = ('b', 'g', 'r', 'c', 'm', 'y', 'k', 'w')
    # the pie chart of the data
    plt.pie(x, colors=c, shadow=False)
    #show image
    plt.savefig('fig.png')

#the code should not be changed
if __name__ == '__main__':
    draw()