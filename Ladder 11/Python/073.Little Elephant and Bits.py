x = list(input())
if '0' in x:
    x.remove('0')
else:
    x.remove('1')
print(*x,sep="")