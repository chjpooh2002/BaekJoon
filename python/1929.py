a,b = map(int,input().split())

def prime_set(b):
    c = [True]*(b+1)
    x = int(b**0.5)
    for i in range(2,x+1):
        if c[i]==True:
            for k in range(i+i,b+1,i):
                c[k] = False
    return [i for i in range(a,b+1) if c[i] == True]


for i in prime_set(b):
    if i!=1:
        print(i)
