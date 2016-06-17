#-*- coding:utf-8 -*-
'''
描述：

美国疾病控制与预防中心（CDC）从1973年开始推行全国家庭成长调查（NSFG），目的是收集（美国）“家庭的生活、婚姻状况、生育、避孕和男女健康信息。”
现有从2002年1月到3月收集的调查数据（url为http://112.124.1.3:8060/getData/101.json），包含上万条调查数据，每条数据包括 caseid（标识符）,
 prglength（婴儿第几周出生）, outcome（怀孕结果，1表示活产）, totalwgt_oz（婴儿出生重量，单位盎司）, 
birthord（第几胎,1表示第一胎）, agepreg（怀孕时年龄）, finalwgt（被调查者的统计权重，表明这名调查者所代表的人群在美国总人口中的比例。过采样人群的权重偏低）等信息
另据某研究显示，婴儿出生周数符合方差为16的正态分布，试写函数solve估计婴儿平均出生周数的置信区间（置信水平为95%）。
输入：

调查样本数据，格式为{data":[[1, 1, 39, 1, 141, 1, 33.16, 6448.271111704751], [1, 2, 39, 1, 126, 2, 39.25, 6448.271111704751], ...]}

输出：

[lower,upper]分别代表平均出生周数的估计下限与上限

注意：

（1）婴儿第几周出生数据由于被调查人选填错误等原因出现了一些不合理数据，比如错填了月份（5<prglength<=10），
其他错填（prglength<=5, 10<prglength<=25, prglength>=49）
，对于错填月份的情况，将月份*4.33作为其周数，对于其他错填情况则舍弃此条数据
'''

import urllib2
import scipy.stats as ss
import numpy as np
class Solution:
    def solve(self):
        data = self.getwebdatass()
        dara=eval(data)['data']
        crr=[]
        for i in dara:
            prglength = i[2]
            if 5<prglength and prglength<=10:
                i=prglength*4.33
                crr.append(i)
            elif 25<prglength and prglength<49:
                crr.append(prglength)
        for i in crr:
            crr.remove(i)
            i=float(i)
            crr.append(i)
        n=len(crr)
        p=0.025
        ssans=-ss.norm.ppf(p) 
        tks= 4.0*ssans/np.sqrt(n)
        meanx=self.getMean(crr)
        return[round(meanx-tks,6),round(meanx+tks,6)]
    def getwebdatass(self):
        url = 'http://112.124.1.3:8050/getData/101'
        data = urllib2.urlopen(url).read()
        return data
    def getMean(self,arr):
        return sum(arr)/len(arr)

    
        
so=Solution()
so.solve()


