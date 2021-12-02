n,k = map(int,input().split())
d=[]
for i in range(n):
    a,b = map(int,input().split())
    d.append([a,b])
d = sorted(d,key=lambda l:[-l[0],l[1]])
print(d.count(d[k-1]))