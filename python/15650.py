from itertools import permutations
a,b = map(int,input().split())
x = [c for c in range(1,a+1)]
for j in permutations(x,b):
    min = j[0]
    count = 0
    for k in range(1,b):
        if min>j[k]:
            count+=1
            break
        else:
            min = j[k]
    if count ==0:
        print(*j)