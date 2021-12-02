x = int(input())
a = list(map(int,input().split()))
y = int(input())
b = list(map(int,input().split()))
f=[]
for i in b:
    for j in a:
        if i%j==0:
            f.append(i/j)
print(f.count(max(f)))