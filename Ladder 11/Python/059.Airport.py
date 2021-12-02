n,m = map(int,input().split())
l = list(map(int,input().split()))
l = sorted(l)
k=[]
i=0
while m:
    for j in range(l[i],0,-1):
        k.append(j)
    i+=1
    m-=1
print(sum(sorted(k,reverse=True)[:n]),sum(k[:n]))