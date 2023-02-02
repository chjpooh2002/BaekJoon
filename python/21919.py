import sys
input = sys.stdin.readline
import math

n=int(input())

def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    if n==1:
        return 0
    return 1

a = list(map(int,input().split()))
b=[]
x=1
count=0
for i in a:
    if is_prime(i):
        count+=1
        if i not in b:
            b.append(i)
for j in b:
    x*=j
if count==0:
    print(-1)
else:
    print(x)
    
        