import sys
input = sys.stdin.readline

n=int(input())
x={}
for i in range(n):
    a=list(map(int,input().split()))
    if a[0] not in x:
        x[a[0]] = [a[1]]
    else:
        x[a[0]].append(a[1])

y = sorted(x.keys())
for i in y:
    x[i].sort()
    for j in x[i]:
        print(i,j)