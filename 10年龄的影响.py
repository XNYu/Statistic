import urllib2
class Solution:
    def solve(self):
        url='http://112.124.1.3:8060/getData/101.json'
        data=urllib2.urlopen(url).read()
        babyArr=eval(data)['data']
        weight=[]
        age=[]
        for i in babyArr:
            weight.append(i[4])
            age.append(i[6])
        lxy,lxx=0.0,0.0
        meanx=sum(age)/float(len(age))
        meany=sum(weight)/float(len(weight))
        for i in range(len(age)):
            lxx+=(age[i]-meanx)**2
            lxy+=(age[i]-meanx)*(weight[i]-meany)
        b=lxy/lxx
        a=meany-b*meanx
        sr,st=0.0,0.0
        for i in range(len(age)):
            sr+=(a+b*age[i]-meany)**2
            st+=(weight[i]-meany)**2
        r2=sr/st
        return[round(a,6),round(b,6),round(r2,6)]
s = Solution()
print s.solve()