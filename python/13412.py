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

n=int(input())
for i in range(n):
    count=0
    number=int(input())
    x=get_divisor(number)
    if len(x)%2==1:
        k=len(x)//2+1
    else:
        k=len(x)//2
    for j in range(k):
        if math.gcd(x[j],x[-1-j])==1:
            count+=1
    print(count)

    