from scipy.stats import t
class Solution():
    def ttest_1samp(self, a, popmean):
        mean,s=0.0,0.0
        mean=sum(a)/float(len(a))
        for i in a:
            s+=(i-mean)**2
        s/=(len(a)-1)
        s=s**0.5
        T=(mean-popmean)/(s/(len(a))**0.5)
        P=t.sf(abs(T),len(a)-1)*2
        return[round(T,6),round(P,6)]
s=Solution()
a=[1,2,3]
pop = 2
print s.ttest_1samp(a,pop)