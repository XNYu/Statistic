from scipy.stats import f

class Solution():
    def f_oneway(self, *args):
        if args[0]==None:
            return [None,None]
        result=[]
        n=len(args)*len(args[0])
        m=len(args)
        fS=m-1
        fe=n-m
        SA=self.getSA(*args)
        Se=self.getSe(*args)
        VA=SA/fS
        Ve=Se/fe
        FA=VA/Ve
        F=f(fS,fe)
        p=F.sf(FA)
        result.append(float('%.6f'%FA))
        result.append(float('%.6f'%p))
        return [float('%.6f'%FA),float('%.6f'%p)]

    def getSe(self,*args):
        result=0
        r=len(args[0])
        m=len(args)
        xi_avg=[]
        for i in range(m):
            temp=args[i]
            avg_t=0
            for j in range(r):
                avg_t+=temp[j]
            avg_t=avg_t/r
            xi_avg.append(avg_t)
        for i in range(m):
            temp=args[i]
            for j in range(r):
                result+=(temp[j]-xi_avg[i])**2
        return result
    
    def getSA(self,*args):
        result=0
        r=len(args[0])
        m=len(args)
        x_avg=0
        xi_avg=[]
        for i in range(m):
            temp=args[i]
            avg_t=0
            for j in range(r):
                x_avg+=temp[j]
                avg_t+=temp[j]
            avg_t=avg_t/r
            xi_avg.append(avg_t)
        x_avg=x_avg/(m*r)
        for i in range(m):
            result+=(xi_avg[i]-x_avg)**2
        result=result*r
        return result

s=Solution()
print(s.f_oneway([1.0,2.0,3.0],[2.0,2.0,3.0]))

    
