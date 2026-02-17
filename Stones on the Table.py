n = int(input().strip())
s = input().strip()

r = 0

for i in range(1, n):
    if s[i] == s[i - 1]:
        r += 1

print(r)
