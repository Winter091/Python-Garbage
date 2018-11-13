def get_dividers(n):
    res = []
    cur_num = n
    probe = 2

    while cur_num != 1:
        if cur_num % probe:
            probe += 1
        else:
            cur_num //= probe
            res.append(probe)

    return res


def get_every_divider_count(divs):
    all_divs = 1

    div_set = set(divs)

    for div in div_set:
        all_divs *= divs.count(div) + 1

    return all_divs


n = int(input())

max_divs_count = 0
max_num = 0

if n == 0:
    print(0)
    print(0)
    exit()
elif n == 1:
    print(1)
    print(1)
    exit()
elif n == 2:
    print(2)
    print(2)
    exit()

if n < 10000:
    for i in (i for i in range(max(0, n - 29000), n) if not i % 2):
        if i == 0:
            count = 0
        elif i == 1:
            count = 1
        else:
            count = get_every_divider_count(get_dividers(i))

        if count > max_divs_count:
            max_num = i
            max_divs_count = count

else:
    for i in (i for i in range(max(0, n - 29000), n) if not i % 5):
        if i == 0:
            count = 0
        elif i == 1:
            count = 1
        else:
            count = get_every_divider_count(get_dividers(i))

        if count > max_divs_count:
            max_num = i
            max_divs_count = count

print(max_num)
print(max_divs_count)