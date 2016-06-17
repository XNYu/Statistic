from math import exp
from math import pi
import random
class Solution:
    def solve(self,a,b):
        if(a<b):
            n = 100000
            k = 0
            Y = exp(-a**2/2)/(2*pi)**0.5
            for i in range(n):
                x = random.uniform(a,b)
                X = exp(-x**2/2)/(2*pi)**0.5
                y = random.uniform(0,Y)
                if(X>y):
                    k+=1
            return round(Y*(b-a)*k/n,6)
        else:
            return None
#if __name__ =="__main__":
#    solution = Solution()
#    print solution.solve(1,2)
