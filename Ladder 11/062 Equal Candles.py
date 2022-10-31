t=int(input())
while(t!=0):
    n=int(input())
    lst=input().split(' ')
    for i in range(n):
        lst[i]=int(lst[i])
    x=min(lst)
    s=0
    for i in range(n):
        s+=lst[i]-x
    print(s)
    t-=1
