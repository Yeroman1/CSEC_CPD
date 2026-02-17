n=int(input())
l=list(map(int, input().split()))
s,d=0,0
for i in range(n):
    if i%2==0:
        s+=max(l[0],l[-1])
        l.remove(max(l[0],l[-1]))
    else:
        d+=max(l[0],l[-1])
        l.remove(max(l[0],l[-1]))

print(s,d)
