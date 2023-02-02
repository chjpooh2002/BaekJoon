from itertools import permutations
a,b = map(int,input().split())
x = [c for c in range(1,a+1)]
for j in permutations(x,b):
    for k in range(b):
        print(j[k],end=" ")
    print()
