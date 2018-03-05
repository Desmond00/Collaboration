'''
import random
import math

def isRepeat(subsets, tempSet):
    print(subsets)
    print(tempSet)
    for subset in subsets:
        valueSet = set()
        for feature in subset:
            valueSet.add(feature)
    for feature in tempSet:
        if((feature in valueSet) == False):
            return False

    
a = 1
Tmax = 4
subsets = []
X = random.sample(range(1,len(xScaled_df.columns)),3)
P = X
subsets.append(X)
r1 = a

i = 0
while i<Tmax:
    subset = []
    s = int(round(random.random(),1)*10)
    r2 = random.uniform(0.0,2.0)
    r3 = random.uniform(0.0,2.0)
    r1 = a - i*(a/Tmax)
    for j in range(3):
        print(X[j])
        if(s%2 == 0):
            feature = int(X[j] + r1*math.sin(r2)*abs(r3*P[j]-X[j]))
        else:
            feature = int(X[j] + r1*math.cos(r2)*abs(r3*P[j]-X[j]))
        subset.append(feature)
    if(isRepeat(subsets, subset) == False):
        X = subset
        subsets.append(subset)
        i += 1
    
print(subsets)
#This is the set of subsets without repeatation of features
'''

import random
import math

def isRepeat(subsets, tempSet):
    print(subsets)
    print(tempSet)
    for subset in subsets:
        valueSet = set()
        for feature in subset:
            valueSet.add(feature)
    for feature in tempSet:
        if((feature in valueSet) == False):
            return False

#MODIFIED r2, r3 ranges. It does the exploration part pretty good. Now we have to develop the whole algorithm including model training and prediction score evaluation.

a = 1
Tmax = 4
subsets = []
totalFeatures = len(xScaled_df.columns)
X = random.sample(range(1,totalFeatures),3)
P = X
subsets.append(X)
r1 = a

i = 0
while i<Tmax:
    subset = []
    s = int(round(random.random(),1)*10)
    r2 = random.uniform(0.1, 1.0)
    r3 = random.uniform(0.1,2.0)
    r1 = a - i*(a/Tmax)
    for j in range(3):
        print(X[j])
        if(s%2 == 0):
            feature = int(X[j] + r1*r2*abs(r3*P[j]-X[j]))
        else:
            feature = int(X[j] + r1*r2*abs(r3*P[j]-X[j]))
        feature %= totalFeatures
        feature += 1
        subset.append(feature)
    if(isRepeat(subsets, subset) == False):
        X = subset
        subsets.append(subset)
        i += 1
    
print(subsets)
#This is the set of subsets without repeatation of features
