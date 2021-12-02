s,n=map(int,input().split())
a=[]
for _ in range(n):
    a.append(list(map(int,input().split())))
b=sorted(a)
for x,y in b:
    if s<=x:
        print('NO')
        break
    else:
        s+=y
else:
    print('YES')