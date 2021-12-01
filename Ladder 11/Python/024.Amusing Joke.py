from collections import Counter
t = list(input())
t += list(input())
r = list(input())
if Counter(t)==Counter(r):
    print("YES")
else:
    print("NO")