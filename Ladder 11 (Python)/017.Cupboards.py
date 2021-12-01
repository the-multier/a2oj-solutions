t = int(input())
l =[]
r =[]
y=x=z=0
for i in range(t):
    a,b = map(int,input().split())
    l.append(a)
    r.append(b)
y = l.count(0)
x = l.count(1)
z += l.count(1) if y>x else l.count(0)
y = r.count(0)
x = r.count(1)
z += r.count(1) if y>x else r.count(0)
print(z)