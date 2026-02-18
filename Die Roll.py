y, w = map(int, input().split())
a = 6 - max(y, w) + 1
b = 6

g = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        g = i

print(str(a//g) + "/" + str(b//g))
