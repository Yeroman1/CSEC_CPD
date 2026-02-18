n = int(input())
h = []
g = []

for _ in range(n):
    a, b = map(int, input().split())
    h.append(a)
    g.append(b)

c = 0

for x in h:
    for y in g:
        if x == y:
            c += 1

print(c)
