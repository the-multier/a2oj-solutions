n=int(input())
a=sum(map(int,input().split()))
print(sum((a+i)%(n+1)!=1 for i in range(1,6)))