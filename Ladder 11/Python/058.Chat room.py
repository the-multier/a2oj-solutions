x = input()
x = x.lower()
s = "hello"
n=0
for i in x:
    if i==s[n]:
        n+=1
    if n==5:
        print("YES")
        break
else:print("NO")