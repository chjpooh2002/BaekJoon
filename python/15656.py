from itertools import product
import sys
input = sys.stdin.readline

a,b = map(int,input().split())
x = list(map(int,input().split()))
x.sort()
for j in product(x,repeat=b):
    print(*j)