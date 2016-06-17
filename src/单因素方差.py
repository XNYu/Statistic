#-*- coding:utf-8 -*-

class Solution():
    def f_oneway(self, *args):
        if args[0]==None:
            return [None,None]
        a=args
        n=0
        for a in args:
            n+=len(a)
        arrlen=len(args[0])
        arglen=len(args)
        As=self.getXi(args)
        print As
        QA=0.0
        for i in range(arglen):
            QA=QA+As[i]*As[i]
        QA=QA/arrlen
        QT=0.0
        for i in range(arglen):
            for j in range(arrlen):
                QT=QT+args[i][j]*args[i][j]
        c=0
        for i in As:
            c+=i
        c=c*c/n
        ST=QT-c
        SA=QA-c
        Se=ST-SA
        F=(SA/(arglen-1))/(Se/(n-arglen))
        print F
    def getXi(self,args):
        total=0
        arr=[]
        arglen=len(args)
        for i in range(arglen):
            for a in args[i]:
                total+=a
            arr.append(total)
        return arr
#     def getQT(self,*args):
#         total=0
#         for a in args:
#             for i in a:
#                 
#                 total+=i**2.0
#         return total
#     def getxi2(self,*args):
#         ans=0
#         for a in args:
#             total=0
#             for i in a:
#                 total+=i
#             total=total/len(a)
#             ans+=total*total
#         return ans
s=Solution()
s.f_oneway([1.0,2.0,3.0],[2.0,2.0,3.0])
                
    
        
        