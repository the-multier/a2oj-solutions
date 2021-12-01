x = int(input())
i=0
x+=1
y = [int(i) for i in str(x)]
while True:
    if len(set(y))==4:
        print(*y,sep='')
        break
    else:
        x+=1
        y = [int(i) for i in str(x)]