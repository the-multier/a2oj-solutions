x = list(input().lower())
y = list(input().lower())
for i,j in zip(x,y):
    if i>j:
        print("1")
        break
    elif i<j:
        print("-1")
        break
else:
    print("0")