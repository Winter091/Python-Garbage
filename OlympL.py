n = int(input())

boys = []
girls = []
for i in range(n):
    t1, t2 = input().split()
    if int(t1):
        girls.append(int(t2))
    else:
        boys.append(int(t2))

boys.sort(reverse=True)
girls.sort(reverse=True)

diff = max_diff = 0

for sex in boys, girls:
    for i in range(len(sex) - 1):
        diff = abs(sex[i] - sex[i + 1])
        if diff > max_diff:
            max_diff = diff

if len(boys) and len(girls):
    if abs(boys[-1] - girls[0]) > max_diff:
        max_diff = abs(boys[-1] - girls[0])

print(max_diff)