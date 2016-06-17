class Solution():
    def describe(self, a):
        if len(a)==1:
            return[a[0],None,0.0,-3.0]
        n=len(a)
        mean=sum(a)/float(len(a))
        s2,s3,s4=0.0,0.0,0.0
        for i in a:
            s2+=(i-mean)**2
            s3+=(i-mean)**3
            s4+=(i-mean)**4
        var=s2/(n-1)
        b2=s2/n
        if s2==0:
            return[mean,var,0.0,-3.0]
        s3=s3/n/b2**1.5
        s4=s4/n/b2**2
        return[round(mean,6),round(var,6),round(s3,6),round(s4-3,6)] 
b = [1.0,8.6,1.1,4.8,2.6,0.7,3.1,1.8,3.5,4.8]
p=Solution()
print p.describe(b)