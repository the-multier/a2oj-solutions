n = int(input())
x = map(int,input().split())
from collections import Counter as co
y = co(x)
# print(y)
k,l = min(y),max(y)
if k==l:
    print(abs(k-l),n*(n-1)//2)
else:
    print(abs(k-l),y[k]*y[l])