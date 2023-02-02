from itertools import permutations
a,b = map(int,input().split())
x = list((map(int,input().split())))
y=sorted(x)
z=set(permutations(y,b))
for j in permutations(y,b):
    if j in z:
        print(*j)
        z.remove(j)