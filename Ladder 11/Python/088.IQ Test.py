x = [list(input()) for _ in range(4)]
u=0
for k in range(3):
        for j in range(3):
            z = x[k][j:j+2]+x[k+1][j:j+2]
            if z.count('#') >= 3 or z.count('.')>=3:
                print("YES")
                u=1
                break
        if u:
            break
else:
    print("NO")