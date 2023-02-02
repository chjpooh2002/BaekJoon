from itertools import combinations
import sys
import math
input = sys.stdin.readline

n=int(input())
for i in range(n):
    sum=0
    z=list(map(int,input().split()))
    z.pop(0)
    for j in combinations(z,2):
        k=list(j)
        p=math.gcd(k[0],k[1])
        sum+=p
    print(sum)
        
    