import urllib2
from scipy.stats import norm as N

class Solution:
    def solve(self):
        url = 'http://112.124.1.3:8050/getData/101'
        data = urllib2.urlopen(url).read()
        
        babyArr = eval(data)['data']
        baby=[]
        for i in babyArr:
            if i[2]>5 and i[2]<=10:
                baby.append(i[2]*4.33)
            if i[2]<49 and i[2]>25:
                baby.append(i[2])
        mean=sum(baby)/float(len(baby))
        print mean
        z=-N.ppf(0.025)
        lower=mean-z*4/(len(baby)**0.5)
        higher=mean+z*4/(len(baby)**0.5)
        print[round(lower,6),round(higher,6)]

so=Solution()
so.solve()