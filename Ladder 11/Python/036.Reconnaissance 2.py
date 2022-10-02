n = int(input())
s = list(map(int,input().split()))
l=len(s)
s.append(s[0])
y=max(s)
c=[]
for i in range(l):
    if y> abs(s[i]-s[i+1]):
        y= abs(s[i]-s[i+1])
        c=[(i),(i+1)%l]
print(c[0]+1,c[1]+1)