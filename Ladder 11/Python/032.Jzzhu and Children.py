n,m = map(int,input().split())
x = list(map(int,input().split()))
d = {}
s = len(x)
y = [i+1 for i in range(s)]
d = dict(zip(y,x))
i=1
if s>1:
    while 1:
        if d[i]>0:
            d[i] -= m
        i+=1
        i%=(s+1)
        if i==0:
            i+=1
        if sum([l>0 for k,l in d.items()])<2:
            break
    for u,v in d.items():
        if v>0:
            print(u)
else:
    print(1)