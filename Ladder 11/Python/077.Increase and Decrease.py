n=int(input())
if sum(map(int,input().split()))%n:
  n-=1
print(n)