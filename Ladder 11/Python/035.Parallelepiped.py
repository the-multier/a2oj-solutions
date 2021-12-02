a,b,c = map(int,input().split())
from math import ceil, sqrt 
s = sqrt(a*b/c)
t = sqrt(a*c/b)
r = sqrt(b*c/a)
print(ceil(4*(s+t+r)))