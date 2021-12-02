t = int(input())
s = list(map(int,input().split()))
m = sum(s)
f = t%m
g=t
if f==0 :
    i=0
    while True:
        g-=s[i]
        if g<=0:
            print(i+1)
            break
        i+=1
        if i>=7:
            i%=7
else:
    for i in range(7):
        f-=s[i]
        if f<=0:
            print(i+1)
            break