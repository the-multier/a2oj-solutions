t = int(input())
for _ in range(t):
    x = input()
    g = len(x)
    if g<=10:
        print(x)
    else:
        print(x[0],g-2,x[-1],sep='')