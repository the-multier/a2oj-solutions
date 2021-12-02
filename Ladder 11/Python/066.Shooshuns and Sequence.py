n,m=map(int,input().split())
lis=list(map(int,input().split()))
while n and lis[n-1]==lis[-1]:
    n-=1
 
print(n if m>=n+1 else -1)