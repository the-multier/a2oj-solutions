x = input()
from collections import Counter
s = Counter(x)
d = [i for i in s.values() if i%2]
if sum(d)%2 or d==[]:
    print("First")
else:
    print("Second")