x = [[1 for i in range(5)] for i in range(5)]
for i in range(1,4):
    y = list(map(int,input().split()))
    for j in range(1,4):
        if y[j-1]%2==1:
            x[i][j] = 1 if x[i][j]==0 else 0
            x[i][j+1]= 1 if x[i][j+1]==0 else 0
            x[i][j-1]= 1 if x[i][j-1]==0 else 0
            x[i+1][j]= 1 if x[i+1][j]==0 else 0
            x[i-1][j]= 1 if x[i-1][j]==0 else 0
for i in range(1,4):
    for j in range(1,4):
        print(x[i][j],end="")
    print()