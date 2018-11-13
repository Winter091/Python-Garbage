a, b, c, d = (int(x) for x in input().split())

print(max(
    a * b + c * d,
    a * c + b * d,
    a * d + b * c
))