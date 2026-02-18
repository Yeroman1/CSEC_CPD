n = int(input())
a = list(map(int, input().split()))

r = 0  
u = 0  

for x in a:
    if x > 0:
        r += x
    else:
        if r > 0:
            r -= 1
        else:
            u += 1

print(u)
