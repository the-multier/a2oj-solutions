t = int(input())
x=y=z=0
for _ in range(t):
    a,b = map(int,input().split())
    x-=a
    x+=b
    if z<x:
        z=x
print(z)