#-*- coding:utf-8 -*-
from _ast import Num

class Solution():
    def solve(self, A):
        #call function prime
        mm=[]
        for i in A:
            if s.prime(i):
                pass
            else:
                mm.append(i)
        
        print mm

    #judge whether x is prime or not
    def prime(self, x):
        num = x**0.5
        num = int(num)
        for i in range(2,num+1):
            ss = x%i
            if ss == 0:
                return True
        return False
    
s=Solution()
s.solve([23, 45, 76, 67, 17] )
n=0;
for i in range(2,5000):
    if s.prime(i):
        pass
    else:
        print i
        n = n+1
print "n="+str(n)