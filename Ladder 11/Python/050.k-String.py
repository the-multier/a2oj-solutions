n = int(input())
s = sorted(input())
a = s[::n]*n
print(["-1","".join(a)][sorted(a)==s])