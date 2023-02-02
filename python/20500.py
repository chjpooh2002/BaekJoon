import sys
input = sys.stdin.readline

def fac(n):
    x=1
    for i in range(2,n+1):
        x*=i
    return x

def com(n,r):
    return fac(n)//(fac(n-r)*fac(r))

n=int(input())
count=0
for i in range(n):
    sum=5
    sum += 1*i +5*(n-1-i)
    if sum%3==0:
        count+=com(n-1,i)
    
print(count%1000000007)