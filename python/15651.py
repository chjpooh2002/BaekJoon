from itertools import product
a,b = map(int,input().split())
x = [c for c in range(1,a+1)]
for j in product(x,repeat=b):
    print(*j)