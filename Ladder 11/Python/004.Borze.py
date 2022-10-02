x = input()
c=[]
while True:
    if x[0]==".":
        c.append(0)
        x=x[1:]
    elif x[:2]=="-.":
        c.append(1)
        x = x[2:]
    elif x[:2]=="--":
        c.append(2)
        x = x[2:]
    if x == "":
        break
print(*c,sep="")