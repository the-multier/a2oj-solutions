x = list(input().replace(" ",""))
y = list(input().replace(" ",""))
from collections import Counter
x = Counter(x)
y = Counter(y)
for i,j in y.items():
    if i in x:
        if j<=x[i]:
            pass
        else:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")