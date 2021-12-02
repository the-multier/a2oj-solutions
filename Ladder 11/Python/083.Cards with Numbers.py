import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
n=int(input());l=list(map(int,input().split()))
d={}
for i in range(2*n):
    d.setdefault(l[i],[]).append(i+1)
if all(i%2==0 for i in list(map(len,d.values()))):
    for i in d:
        print("\n".join("{0} {1}".format(*k) for k in zip(d[i][::2],d[i][1::2])))
else:
    print(-1)