n,m = map(int,input().split())
x = list(map(int,input().split()))
c = [i for i in x if i<0]
c.sort()
if m>=len(c):
    print(abs(sum(c)))
else:
    print(abs(sum(c[:m])))