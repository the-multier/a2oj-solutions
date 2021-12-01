a =[]
h=0
x=y=0
for i in range(5):
    a.append(list(map(int,input().split())))
for i,j in enumerate(a):
    for k,l in enumerate(j):
        if l==1:
            x,y = i+1,k+1
            h= 1
            break
    if h==1:
        break
print(abs(3-x)+abs(3-y))