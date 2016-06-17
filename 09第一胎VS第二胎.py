import urllib2
from scipy.stats import chi2
class Solution:
    def solve(self):
        url='http://112.124.1.3:8060/getData/101.json'
        data=urllib2.urlopen(url).read()
        babyArr=eval(data)['data']
        baby=[]
        num=[]
        for i in babyArr:
            if i[2]<=10 and i[2]>5:
                baby.append(i[2]*4.33)
                num.append(i[5])
            if i[2]<49 and i[2]>25:
                baby.append(i[2])
                num.append(i[5])
        a1,a2,a3,n1,n2,n3=0.0,0.0,0.0,0.0,0.0,0.0
        for i in range(len(baby)):
            if baby[i]<=37:
                a1+=1
                if num[i]==1:
                    n1+=1
            elif baby[i]>=41:
                a3+=1
                if num[i]==1:
                    n3+=1
            else:
                a2+=1
                if num[i]==1:
                    n2+=1
        a=a1+a2+a3
        p1=a1/a
        p2=a2/a
        p3=a3/a
        n=n1+n2+n3
        c=n1**2/(n*p1)+n2**2/(n*p2)+n3**2/(n*p3)-n
        p=chi2.sf(c,2)
        print[c,p]
        
s=Solution()
s.solve()
        