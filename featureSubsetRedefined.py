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
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier

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

def trainTestScore(data):
    data = pd.read_csv("pimaIndiansDiabetes.csv")
    X = data.drop('1', axis=1)
    y = data['1']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33)
    errorRate = []
    for i in range(40):
        knn = KNeighborsClassifier(n_neighbor = i)
        knn.fit(X_train, y_train)
        prediction = knn.predict(X_test)
        errorRate.append(np.mean(prediction != y_test))
    plt.plot(range(1,40), errorRate, color='blue', linestyle='dashed', marker='o',
     markerfacecolor='red', markersize=12)

#SCA

a = 1
Tmax = 6
subsets = []
totalFeatures = len(X.columns)
X = random.sample(range(1,totalFeatures),3)  
P = 100
t = 0
while t<Tmax :

totalFeatures = len(X.columns)
X = random.sample(range(1,totalFeatures),3)
subsets = []
subsets.append(X) 
def randomSearchAgents(m, n):
    i = 1
    while i<m:
        X = random.sample(range(1,totalFeatures),3)
        if (isRepeat(subsets, X) == False):
            subsets.append(X)
            i += 1