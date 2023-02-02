import sys
input = sys.stdin.readline

p=1000000007
def power(num, p, mod):
    if p == 1:
        return num % mod
    
    if p % 2:
        return ((power(num,p//2,mod) ** 2) * num) % mod
    else:
        return (power(num,p//2,mod) ** 2) % mod
        
def fac(num, mod):
    result = 1
    for i in range(2, num+1):
        result = result * i % p
    return result

n,k=map(int,input().split())
a=fac(n,p)

print(a*power(fac(k,p)*fac(n-k,p),p-2,p)%p)
