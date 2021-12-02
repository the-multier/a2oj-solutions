t = int(input())
s = list(map(int,input().split()))
m = min(s)
if s.count(m)==1:
	print(s.index(m)+1)
else:
	print("Still Rozdil")