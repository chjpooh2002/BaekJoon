from itertools import combinations_with_replacement
a,b = map(int,input().split())
x = [c for c in range(1,a+1)]
for j in combinations_with_replacement(x,b):
    print(*j)