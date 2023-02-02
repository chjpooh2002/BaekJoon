n,m = map(int,input().split())
def pec(n):
    x = 1
    for i in range(1,n+1):
        x*=i
    return x

def combination(n,m):
    return pec(n)//(pec(m)*pec(n-m))

print(combination(n,m))
        