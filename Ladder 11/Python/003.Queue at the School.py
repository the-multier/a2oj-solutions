x,y = map(int,input().split())
a = list(input())
i=0
for _ in range(y):
    while i<x-1:
        if a[i]=="B" and a[i+1]=="G":
            a[i],a[i+1]="G","B"
            i+=1
        i+=1
    i=0
print(*a,sep='')