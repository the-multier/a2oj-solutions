t = int(input())
g=0
for _ in range(t):
    x = list(map(int,input().split()))
    if x.count(1)>=2:
        g+=1
print(g)