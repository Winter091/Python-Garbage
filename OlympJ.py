a = input().split()
if int(a[0]) * int(a[1]) < int(a[2]) * int(a[3]):
    print('P')
else:
    b = 'M' if int(a[0]) * int(a[1]) > int(a[2]) * int(a[3]) else 'E'
    print(b)

for i in range(10,step=-1):
    print(i)