x = int(input())
y = map(int,input().split())
t=0
j=1
for i in sorted(y):
    t+= abs(i-j)
    j+=1
print(t)