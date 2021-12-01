n, k, l, c, d, p, nl, np = map(int,input().split())
# print(k*l//n,c*d,p/np)
print("%d" % (min(k*l//nl,c*d,p/np)//n))