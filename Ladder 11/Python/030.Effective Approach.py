n=int(input());d={}
for i,j in enumerate(map(int,input().split())):
	d[j]=i+1
m=int(input());v,p=0,0
for i in map(int,input().split()):
	v+=d[i];p+=n-d[i]+1
print(v,p)