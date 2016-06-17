import random
import math

class Solution:
    def getNum(self,x):
        a=math.pow(x, 2)
        a=-a/2
        b=math.exp(a)
        c=math.pi
        d=math.sqrt(c)
        e=math.sqrt(2)
        f=b/(d*e)
        return f
    def solve(self,a,b):
        total=0
        useful=0
        shuzu=[]
        for i in range(0,1000000) :
            c=random.uniform(a,b)
            c=self.getNum(c)
            shuzu.append(c)
        maax=max(shuzu)
        miin=min(shuzu)
        for i in shuzu:
            total+=1
            d=random.uniform(miin,maax)
            if(d<=i):
                useful+=1
        m=1.0*total
        d=useful/m
        e=(maax-miin)*(b-a)
        m=d*e
        return m
    
solu=Solution()
solu.solve(0.0,10.0)