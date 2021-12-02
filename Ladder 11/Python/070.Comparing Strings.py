x = input()
y = input()
z=0
from collections import Counter
if len(x)==len(y):
    for i,j in zip(x,y):
        # print(i,j)
        if i!=j:
            z+=1
    x = Counter(x)
    y = Counter(y)
    print(["NO","YES"][x==y and z<=2])
else:
    print("NO")