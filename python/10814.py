import sys
input = sys.stdin.readline

n=int(input())
x={}
for i in range(n):
    a=input().split()
    z = int(a[0])
    if z not in x:
        x[z] = [a[1]]
    else:
        x[z].append(a[1])

y = sorted(x.keys())
for i in y:
    for j in x[i]:
        print(i,j)
        