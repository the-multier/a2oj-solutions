n = int(input())
a = list(map(int,input().split()))
q,w=0,0
for i in a:
	if i ==25:q+=1
	elif i==50:q-=1;w+=1
	else:
		if w>0:w-=1;q-=1
		else:q-=3
	if q<0 or w<0:n=0;break
if n==0:print("NO")
else:print("YES")