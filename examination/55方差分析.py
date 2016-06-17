#-*- coding:utf-8 -*-
from scipy import stats
import numpy as np
from log_api import log

def oneway_anova():
    A1=[27.0, 26.2, 28.8, 33.5, 28.8]
    A2=[22.8, 23.1, 27.7, 27.6, 24.0]
    A3=[21.9, 23.4, 20.1, 27.8, 19.3]
    A4=[23.5, 19.6, 23.7, 20.8, 23.9]

    A=[A1, A2, A3, A4]
    n=20
    As=np.sum(A, axis=1)
    QA=0.0
    for i in range(4):
        QA=QA+As[i]*As[i]
    QA=QA/5
    
    QT=0.0
    for i in range(4):
        for j in range(5):
            QT=QT+A[i][j]*A[i][j]
    
    C=np.sum(A)*np.sum(A)/n
    ST=QT-C
    SA=QA-C
    Se=ST-SA
    F=(SA/3)/(Se/16)
    
    log('QA is ' + str(QA))
    log('QT is ' + str(QT))
    log('C is ' + str(C))
    log('ST is ' + str(ST))
    log('SA is ' + str(SA))
    log('Se is ' + str(Se))
    log('F is '+ str(F))

def twoway_anova():
    pass

#the code should not be changed
if __name__ == '__main__':
        oneway_anova()
        twoway_anova()