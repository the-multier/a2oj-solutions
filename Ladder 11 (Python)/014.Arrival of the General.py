g = int(input())
l = list(map(int,input().split()))
mi = min(l)
ma = max(l)
y=0
for i in l:
    if i == ma:
        break
    y+=1
l.remove(ma)
l.insert(0,ma)
x = l[-1::-1]
for j in x:
    if j==mi:
        break
    y+=1
print(y)