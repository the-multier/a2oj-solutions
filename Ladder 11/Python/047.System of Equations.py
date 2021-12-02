a,b = map(int,input().split())
s=t=0
for i in range(a+1):
    for j in range(b+1):
        if i**2+j==a and j**2+i==b:
            # print("a",i,j)
            s+=1
print(s)