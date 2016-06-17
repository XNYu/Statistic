from scipy.stats import chi2
class Solution():
    def independence_test(self, A):
        if len(A)==1:
            return [0.0,None]
        if len(A[0])==1:
            return [0.0,None]
        r = len(A)
        c = len(A[0])
        x = []
        y = []
        n = 0.0
        C = 0.0
        for i in A:
            x.append(sum(i))
        for i in A[0]:
            y.append(0.0)
        for i in range(r):
            for j in range(c):
                y[j]+=A[i][j]
                n+=A[i][j]
        for i in range(r):
            for j in range(c):
                C+=((A[i][j]-x[i]*y[j]/n)**2)/(x[i]*y[j]/n)
        P = chi2.sf(C,(c-1)*(r-1))
        return[round(C,6),round(P,6)]
s = Solution()
print s.independence_test( [[1.0,2.0,3.0],[2.0,2.0,3.0]])