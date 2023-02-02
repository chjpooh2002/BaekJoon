import sys
input = sys.stdin.readline

n,m=map(int,input().split())
x={}
for i in range(n):
    y=input().split()
    a1=y[0]
    a2=y[1]
    x[a1]=a2
for i in range(m):
    k=input().split("\n")
    print(x[k[0]])