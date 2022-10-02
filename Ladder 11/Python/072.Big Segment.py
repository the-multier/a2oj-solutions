d = [tuple(map(int,input().split())) for _ in range(int(input()))]
x = min(i[0] for i in d)
y = max(i[1] for i in d)
print(d.index((x,y))+1 if (x,y) in d else "-1")