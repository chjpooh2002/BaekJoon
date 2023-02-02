import sys
import math
input = sys.stdin.readline

def get_divisor(n):
    n = int(n)
    divisors = []
    divisors_back = [] 

    for i in range(1, int(n**(1/2)) + 1): 
        if (n % i == 0):            
            divisors.append(i)
            if (i != (n // i)): 
                divisors_back.append(n//i)

    return divisors + divisors_back[::-1]

r,g=map(int,input().split())
x=get_divisor(math.gcd(r,g))
for i in x:
    print(f'{i} {r//i} {g//i}')