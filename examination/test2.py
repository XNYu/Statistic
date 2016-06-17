import string
class Solution():
    def solve(self, A):
        sss={}
        for ss in A:
            print ss
            ss=str(ss)
            sm = list(ss)
            print sm
            
            for s in sm:
                if sss.has_key(s):
                    sss[s] = sss[s]+1
                else:
                    sss[s] = 1
        print sss
    
s = Solution();
s.solve(['12','34','567', '36','809','120']  )