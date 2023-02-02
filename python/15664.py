from itertools import combinations
a,b = map(int,input().split())
x = list((map(int,input().split())))
y=sorted(x)
z=set(combinations(y,b))
for j in combinations(y,b):
    if j in z:
        print(*j)
        z.remove(j)