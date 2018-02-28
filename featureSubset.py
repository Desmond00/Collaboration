import random
import math

def isRepeat(subsets, tempSet):
    #print(subsets)
    #print(tempSet)
    for subset in subsets:
        valueSet = set()
        for feature in subset:
            valueSet.add(feature)
        for feature in tempSet:
            if((feature in valueSet) == False):
                return False

    
a = 1

subsets = []
subsets.append(random.sample(range(1,len(xScaled_df.columns)),3))
r1 = a
s = int(round(random.random(),1)*10)

for i in range(4):
    subset = []
    for j in range(3):
        r2 = random.uniform(0.0,2.0)
        r3 = random.uniform(0.0,2.0)
        if(s%2 == 0):
            feature = int(x[j] + r1*math.sin(r2)*abs(r3*x[j]-x[j]))
        else:
            feature = int(x[j] + r1*math.cos(r2)*abs(r3*x[j]-x[j]))
        r1 = a - j*(a/3)
        subset.append(feature)
    if(isRepeat(subsets, subset) == False):
        subsets.append(subset)
    
print(subsets)
#This is the set of subsets without repeatation of features
