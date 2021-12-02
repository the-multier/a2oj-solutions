a = int(input())
s = list(map(int,input().split()))
s.sort(reverse=True)
t=0
if a<=0:print("0")
else:
    for i,j in enumerate(s):
        t+=j
        if t>=a:
            print(i+1)
            break
    else:
        print("-1")