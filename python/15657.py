from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

a,b = map(int,input().split())
x = list(map(int,input().split()))
x.sort()
for j in combinations_with_replacement(x,b):
    print(*j)