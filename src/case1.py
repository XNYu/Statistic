#-*- coding:utf-8 -*-
class Solution():
    def describe(self, a):
        length=len(a)
        xave=self.ave(a)
        fc=self.getCifang(a, xave, 2)
        if(length==0):
            xave=0
            fcxz=0
            pd=0
            fd=-3
        if(length==1):
            fcxz=fc
            pd=0
            fd=-3
        else:
            fcxz=fc*length/(length-1)
            pd=self.getCifang(a, xave, 3)/(fc**(3./2))
            fd=self.getCifang(a, xave, 4)/(fc**2./1)-3
        arr=[]
        arr.append(xave)
        arr.append(fcxz)
        arr.append(pd)
        arr.append(fd)
        return arr
    def ave(self,a):
        b=0
        for i in a:
            b+=i
        b=1.0*b
        return b/a.__len__()
    def getCifang(self,a,xave,cishu):
        b=0
        lenth=0.0
        for i in a:
            b+=((i-xave)**cishu)
            lenth+=1
        return b/lenth
