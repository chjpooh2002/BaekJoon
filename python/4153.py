import sys
input = sys.stdin.readline

while True:
    sum=0
    a=list(map(int,input().split()))
    if a[0]==0:
        break
    x=max(a)
    y=min(a)
    a.remove(x)
    a.remove(y)
    z=a[0]
    if y**2+z**2==x**2:
        print("right")
    else:
        print("wrong")