s = int(input())
e=[]
t=0
for _ in range(s):
    e.append(list(map(int,input().split())))
for i,j in e:
    a=b=c=d= False
    for u,v in e:
        if u==i and v==j:
            continue
        if u>i and v==j:
            a = True
        if u<i and v==j:
            b = True
        if u==i and v<j:
            c = True
        if u==i and v>j:
            d = True
    if a and b and c and d:
        t+=1
print(t)