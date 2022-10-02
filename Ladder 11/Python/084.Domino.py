u = []
d = []
for i in range(int(input())):
    a,b = map(int,input().split())
    u.append(a%2)
    d.append(b%2)
if sum(u)%2==0 and sum(d)%2==0:
    print(0)
else:
    for i in range(len(u)):
        if u[i]==0 and d[i]==1:
            u[i],d[i] = d[i],u[i]
        elif u[i]==1 and d[i]==0:
            u[i],d[i] = d[i],u[i]
        if sum(u)%2==0 and sum(d)%2==0:
            print(1)
            break
    else:
        print(-1)