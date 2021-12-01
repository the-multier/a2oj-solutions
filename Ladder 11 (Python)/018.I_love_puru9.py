t = int(input())
x = list(map(int,input().split()))
a=b=x[0]
c=0
for i in x:
    if i>a:
        c+=1
        a=i
    if i<b:
        c+=1
        b=i
print(c)