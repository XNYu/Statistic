class Solution():
    def solve(self, A):
        #use isPalindrom function to check if the string is palindrome or not
        sss=[]
        for ss in A:
            if s.isPalindrome(ss):
              sss.append(ss)
        print sss  
        pass

    def isPalindrome(self, x):
        mm = list(x)
        long = mm.__len__()
        if (long==1)|(long==0):
            return True
        else:
            if(mm[0]==mm[long-1]):
                del mm[long-1]
                del mm[0]
                return s.isPalindrome(mm)
            else:
                return False
            
        pass
        
    
    
s =Solution()
print s.solve(['123', '232', '4556554','12123', '3443','1314131'] )

