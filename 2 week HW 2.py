n = int(input('введите целое число: '))
s = []

for i in range(1, n+1):
    s.append(i)
if len(s) % 2 == 0:
    i = 0
    while i < len(s):
        newlist = s[i]
        s[i] = s[i+1]
        s[i+1] = newlist
        i += 2
else:
    i = 0
    while i < len(s) - 1:
        newlist = s[i]
        s[i] = s[i + 1]
        s[i + 1] = newlist
        i += 2
print(s)






