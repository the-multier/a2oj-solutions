n,m=map(int,input().split())
a=[input() for i in range(n)]
# print(a)
c=[]
for i in range(n):
    if i%2==0:
        if m%2:
            d = "BW"*(m//2)+"B"
        else:
            d = "BW"*(m//2)
    else:
        if m%2:
            d = "WB"*(m//2)+"W"
        else:
            d = "WB"*(m//2)
    c.append(d)
for i,g in zip(a,c):
    for j,h in zip(i,g):
        if j=='-':
            print(j,end="")
        else:
            print(h,end="")
    print()