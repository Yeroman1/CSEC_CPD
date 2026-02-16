l, b = map(int, input().split())
y=0
while(l<=b):
    l*=3
    b*=2
    y=y+1
print(y)
