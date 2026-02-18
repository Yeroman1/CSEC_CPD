a, b, c, d = map(int, input().split())
s = input()

t = 0
for x in s:
    match x:
        case "1":
            t += a
        case "2":
            t += b
        case "3":
            t += c
        case "4":
            t += d

print(t)
