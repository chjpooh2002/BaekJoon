from itertools import combinations_with_replacement
a,b = map(int,input().split())
x = list((map(int,input().split())))
y=sorted(x)
z=set(combinations_with_replacement(y,b))
for j in combinations_with_replacement(y,b):
    if j in z:
        print(*j)
        z.remove(j)