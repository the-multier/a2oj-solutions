x = int(input())
g=0
for _ in range(x):
    if "+" in input():
        g+=1
    else:
        g-=1
print(g)