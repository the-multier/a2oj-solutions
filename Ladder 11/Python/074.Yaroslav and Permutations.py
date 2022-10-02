x = int(input())
y = map(int,input().split())
from collections import Counter
import math 
x = math.ceil(x/2)
y = Counter(y)
for i in y.values():
    if i>x:
        # print(x,i)
        print('NO')
        break
else:
    print("YES")