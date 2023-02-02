import sys
input = sys.stdin.readline


def fac(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n,k=map(int,input().split())
com=fac(n) // (fac(k) * fac(n - k))
print(com%10007)






