x,y = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
o=0
if max(a)>=min(b):
    print(-1)
else:
    o = max(max(a),2*min(a))
    if o>=min(b):
        print(-1)
    else:
        print(o)