x,y = map(int,input().split())
np = x+1
while True:
    j=0
    for i in range(2,np+1):
        if np%i==0:
            j+=1
        if j>1:
            break
    else:
        break
    j=0
    np+=1
if y == np:
    print("YES")
else:
    print("NO")