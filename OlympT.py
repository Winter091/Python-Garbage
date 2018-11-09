k = input()

a = 0; b = 0; c = 0
for i in range(len(k)):
    if k[i] == '0':
        a += 1
    else:
        if c:
            b += a
            a = 0
        c = 1
print(b)
