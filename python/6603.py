from itertools import combinations
import sys
input = sys.stdin.readline

while True:
    a=list(map(int,input().split()))
    if a[0]==0:
        break
    a.pop(0)
    for i in combinations(a,6):
        print(*i)
    print()
