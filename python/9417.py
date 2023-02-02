from itertools import combinations
import sys
import math
input = sys.stdin.readline

n=int(input())
for i in range(n):
    x=[0]
    z=list(map(int,input().split()))
    for j in combinations(z,2):
        k=list(j)
        p=math.gcd(k[0],k[1])
        if p>x[0]:
            x[0]=p
    print(x[0])