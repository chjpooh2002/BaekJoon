import sys
input = sys.stdin.readline
n=int(input())
x=[int(input()) for i in range(n)]
x.sort()
for i in x:
    print(i)