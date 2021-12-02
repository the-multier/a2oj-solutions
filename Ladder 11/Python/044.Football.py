s = [input() for i in range(int(input()))]
from collections import Counter
c = Counter(s)
k=0
for i,j in c.items():
    if k<j:k=j;f=i
print(f)