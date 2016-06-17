class Solution():
    def getMean(self,a):
        result=0
        for i in range(len(a)):
            result+=a[i]
        return result/len(a)

    def getV(self,a,c):
        result=0
        mean=self.getMean(a)
        for i in range(len(a)):
            result+=(a[i]-mean)**c
        return result/len(a)
    
    def describe(self, a):
        if a==None :
            return None
        if len(a)==1:
            return [a[0],a[0],None,None]
        else:
            result=[]
            mean=self.getMean(a)
            v2=self.getV(a,2)
            v3=self.getV(a,3)
            v4=self.getV(a,4)

            var=v2

            skew=v3/(v2**1.5)

            kurt=(v4/v2**2)-3

            result.append(mean)
            result.append(var)
            result.append(skew)
            result.append(kurt)
        
            return result

s=Solution()
a=[1]
print(s.describe(a))
