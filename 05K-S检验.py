class Solution():
    def ks_2samp(self, data1, data2):
        maxi = 0.0
        minr = min(min(data1),min(data2))
        maxr = max(max(data1),max(data2))
        d = (maxr-minr)/max(len(data1),len(data2))
        n = 1
        while minr+d*n<maxr+d:
            n1 = 0.0
            n2 = 0.0
            for i in data1:
                if i<minr+d*n:
                    n1+=1
            for i in data2:
                if i<minr+d*n:
                    n2+=1
            maxi = max(maxi,abs(n1/len(data1)-n2/len(data2)))  
            n+=1
        print round(maxi,6)
s=Solution()
s.ks_2samp([0,1,2,3], [1,2,3,4])