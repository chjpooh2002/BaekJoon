x = 7368788
a = [False,False]+[True]*(x)
n=int(input())

primes=[]
for i in range(2,x):
  if a[i]:
    primes.append(i)
    for j in range(2*i, x, i):
        a[j] = False
print(primes[n-1])