from scipy.stats import t
class Solution():
    def pearsonr(self, x, y):
        if x==None or y==None or len(x)==0 or len(y)==0:
            return[None,None]
        meanx,meany,sx,sy,r=0.0,0.0,0.0,0.0,0.0
        meanx=sum(x)/float(len(x))
        meany=sum(y)/float(len(y))
        for i in x:
            sx+=(i-meanx)**2
        sx/=float(len(x)-1)
        sx=sx**0.5
        for i in y:
            sy+=(i-meany)**2
        sy/=float(len(y)-1)
        sy=sy**0.5
        for i in range(len(x)):
            r+=(x[i]-meanx)*(y[i]-meany)/sx/sy
        r/=float(len(x)-1)
        return[round(r,6),round(0,6)]
s = Solution()
print s.pearsonr([1.0,2.0,3.0],[2.0,2.0,3.0])