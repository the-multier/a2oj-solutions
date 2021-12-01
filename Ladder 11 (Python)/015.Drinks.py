x = int(input())
v = list(map(int,input().split()))
y= sum(v)
print("%.12f" % (y/len(v)))