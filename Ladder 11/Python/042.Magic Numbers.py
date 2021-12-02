x = input()
while len(x)>0:
    # print(x[:3] , x[3:])
    if x[:3]=="144":
        x = x[3:]
        # print(x)
    elif x[:2]=="14":
        # print("2")
        x = x[2:]
    elif x[:1]=="1":
        # print("3")
        x = x[1:]
    else:
        print("NO")
        break
else:
    print("YES")