from itertools import permutations
a,b = map(int,input().split())
x = list(map(int,input().split()))
x.sort()
for j in permutations(x,b):
    print(*j)