n,m=map(int,input().split())
a=sorted(map(int,input().split()))
print(min(j-i for i,j in zip(a,a[n-1:])))