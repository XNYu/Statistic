# ��·��˾�������еĻ�ͷ�������˱�ţ���1��N����һ���㿴��һ�����Ϊ60�Ļ�ͷ���Ǹ���·��˾���ж��ٻ�ͷ�أ����ü�����Ȼ���ơ���Сƫ������ơ���ƫ���Ʒֱ�����ͷ��Ŀx�����ظ�10000�����飬���������ʡ���ƫ����(x-N)^2����ƫ��(x-N)�����бȽϣ������ֹ��Ʒ�������ȱ�㡣
# ����Ϊ��ͷ�����pythonʵ�֣������������ϰ��
# ��1����ϸ�Ķ��������뺬�壬�����д��룬���������Σ�
# ��2�������㿴���������𳵣���ŷֱ�Ϊ46��24����ô��ν��в��������أ�����ʾ����ι������ƽ��ֵor�޸Ĺ��㹫ʽ����
# ��3�������㿴���˶������������������أ�
#-*- coding:utf-8 -*-
import random
from log_api import log

def number_trans(upper_bound):
    return random.randint(1,upper_bound)

def train_seen(N):
    return random.randint(1,N)

def MLE_estimation(evidence):
    return evidence

def MSE_estimation(evidence):
    return round(1.5*evidence)

def ME_estimation(evidence):
    return 2*evidence

def estimate():
    number_experiments = 10000
    upper_bound = 100
    H1 = H2 = H3 = MSE1 = MSE2 = MSE3 = ME1 = ME2 = ME3 = 0.0
    
    for j in range(number_experiments):
        N = number_trans(upper_bound)
        evidence = train_seen(N)

        hypo1 = MLE_estimation(evidence)
        hypo2 = MSE_estimation(evidence)
        hypo3 = ME_estimation(evidence)

        #calculating hits
        H1 = H1 + 1 if hypo1==N else H1
        H2 = H2 + 1 if hypo2==N else H2
        H3 = H3 + 1 if hypo3==N else H3

        #calculating mean squared error
        MSE1 = MSE1 + (hypo1-N)**2
        MSE2 = MSE2 + (hypo2-N)**2
        MSE3 = MSE3 + (hypo3-N)**2

        #calculating mean error
        ME1 = ME1 + (hypo1-N)
        ME2 = ME2 + (hypo2-N)
        ME3 = ME3 + (hypo3-N)
        
    log(H1/number_experiments)
    log(H2/number_experiments)
    log(H3/number_experiments)
    log(MSE1/number_experiments)
    log(MSE2/number_experiments)
    log(MSE3/number_experiments)
    log(ME1/number_experiments)
    log(ME2/number_experiments)
    log(ME3/number_experiments)


#the code should not be changed
if __name__ == '__main__':
    estimate()