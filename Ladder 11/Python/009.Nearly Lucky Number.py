x = input()
y = x.count("7")
y+=x.count("4")
c = str(y)
if not '7' in c and not '4' in c:
    print("NO")
else:
    print("YES")