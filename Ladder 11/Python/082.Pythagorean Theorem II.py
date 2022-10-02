import math
x=int(input())
s=0
for a in range(1,x):
    for b in range(1,x):
        c = math.sqrt(a*a+b*b)
        if(int(c)==c and c<=x):
            s+=1
print(s//2)