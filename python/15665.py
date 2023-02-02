from itertools import product
a,b = map(int,input().split())
x = list((map(int,input().split())))
y=sorted(x)
z=set(product(y,repeat=b))
for j in product(y,repeat=b):
    if j in z:
        print(*j)
        z.remove(j)