x = input()
c=d=0
for i in list(x):
    if i.islower():
        c+=1
    else:
        d+=1
if d>c:
    print(x.upper())
else:
    print(x.lower())