a,b,c = map(int,input().split())
n=a*b*c+1
d=[1]*n
for i in range(2,n):
    for j in range(i,n,i):
        d[j]+=1
sum=0
for i in range(1,a+1):
    for j in range(1,b+1):
        for k in range(1,c+1):
            sum = sum+d[i*j*k]
print(sum%2**30)