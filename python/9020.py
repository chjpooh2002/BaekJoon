import sys
import math
input = sys.stdin.readline

def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    if n==1:
        return 0
    return 1

n=int(input())
for i in range(n):
    a=int(input())
    for j in range(a//2,1,-1):
        if is_prime(j) and is_prime(a-j):
            print(f'{j} {a-j}')
            break
