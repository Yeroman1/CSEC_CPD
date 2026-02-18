m = []
for i in range(5):
    r = list(map(int, input().split()))
    m.append(r)
    if 1 in r:
        x, y = i, r.index(1)

d = abs(x - 2) + abs(y - 2)
print(d)
