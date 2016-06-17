from scipy.stats import f
class Solution():
    def f_oneway(self, *args):
       if len(args)==0:
            return[None,None]
       elif len(args)==1:
           return[None,None]
       else:
           meanr = []
           mean = 0.0
           sa = 0.0
           se = 0.0
           for i in args:
               meanr.append((float)(sum(i))/len(i))
               mean+=sum(i)
           mean/=(len(args)*len(args[0]))
           for i in meanr:
               sa+=len(args[0])*(i-mean)**2
           for i in range(len(meanr)):
               for j in range(len(args[0])):
                   se+=(args[i][j]-meanr[i])**2
           fa = len(args)-1
           fe = len(args)*len(args[0])-len(args)
           va = sa/fa
           ve = se/fe
           F = va/ve
           P = f.sf(F,fa,fe)    
           return[round(F,6),round(P,6)]
s = Solution()
print s.f_oneway([1.0,2.0,3.0],[2.0,2.0,3.0])
print s.f_oneway([25.6,22.2,28.0,29.8],[24.4,30.0,29.0,27.5],[25.0,27.7,23.0,32.2],[28.8,28.0,31.5,25.9],[20.6,21.2,22.0,21.2])
