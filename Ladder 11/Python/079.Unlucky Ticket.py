m=int(input())
n=(input())
z=zip(sorted(n[:m]),sorted(n[m:]))
 
print(["NO","YES"][abs(sum((i>j)-(j>i)for i,j in z))==m])