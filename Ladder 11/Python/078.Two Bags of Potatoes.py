y,k,n=map(int,input().split())
l=range((k-y)%k or k,n-y+1,k) or (-1,)
print(*l)