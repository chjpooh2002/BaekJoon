from itertools import combinations
import sys
input = sys.stdin.readline

a,b = map(int,input().split())
x = list(map(int,input().split()))
x.sort()
for j in combinations(x,b):
    print(*j)