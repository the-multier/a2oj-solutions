n = int(input())
s = [0]+list(map(int,input().split()))
ss = sorted(s.copy())
for i in range(1,n+1):s[i]+=s[i-1];ss[i]+=ss[i-1]
for _ in range(int(input())):
    t,l,r = map(int,input().split())
    if t==1:
        print(s[r]-s[l-1])
    else:
        print((ss[r]-ss[l-1]))