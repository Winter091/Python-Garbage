a = [int(i) for i in input().split()]

if a[0] * a[1] < a[2] * a[3]:
    print('P')
else:
    b = 'M' if a[0] * a[1] > a[2] * a[3] else 'E'
    print(b)
