x= list(input())
y= list(input())
c=[]
for i,j in zip(x,y):
    if i==j:
        c.append(0)
    else:
        c.append(1)
print(*c,sep='')