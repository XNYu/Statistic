import random
import math
a=[]
b=[]
for c in range(1,40):
    for i in range(1,200):
        a.append(random.randint(1,199))
    b.append(sum(a)/len(a))
print sum(b)/len(b)