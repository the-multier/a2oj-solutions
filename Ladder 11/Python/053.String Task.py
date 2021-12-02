x = input()
a = "AEIOUYyaeiou"
y = ['.'+i.lower() for i in x if i not in a ]
print(''.join(y))