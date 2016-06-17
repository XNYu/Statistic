from scipy.stats import f
class Solution():
    def f_oneway(self, *args):
        if args==None or len(args)==0 or len(args[0])==0:
            return[None,None]
        r = len(args)
        c = len(args[0])
        meanr=[]
        mean,sa,se=0.0,0.0,0.0
        for i in args:
            meanr.append(sum(i)/float(len(i)))
            mean+=sum(i)
        mean/=(r*c)
        for i in range(r):
            sa+=c*(meanr[i]-mean)**2
            for j in range(c):
                se+=(args[i][j]-meanr[i])**2
        fa=r-1
        fe=r*c-r
        va=sa/fa
        ve=se/fe
        F=va/ve
        P=f.sf(F,fa,fe)
        return[round(F,6),round(P,6)]
s = Solution();
print s.f_oneway([1.0,2.0,3.0],[2.0,2.0,3.0])
