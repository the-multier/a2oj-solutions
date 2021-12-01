x = int(input())
y = list(input())
i=u=0
while i<x-1:
    if len(y)<1:
        break
    if y[i]==y[i+1]:
        del y[i+1]
        u+=1
        i-=1
        x-=1
    i+=1
print(u)