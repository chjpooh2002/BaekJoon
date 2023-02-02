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

while True:
    n=int(input())
    count=0
    if n==0:
        break
    for i in range(2,n//2+1):
        if is_prime(i) and is_prime(n-i):
            count+=1
            print(f'{n} = {i} + {n-i}')
            break
    if count==0:
        print("Goldbach's conjecture is wrong.")
    