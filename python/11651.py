import sys
input = sys.stdin.readline

n=int(input())
x={}
for i in range(n):
    a=list(map(int,input().split()))
    if a[1] not in x:
        x[a[1]] = [a[0]]
    else:
        x[a[1]].append(a[0])

y = sorted(x.keys())
for i in y:
    x[i].sort()
    for j in x[i]:
        print(j,i)