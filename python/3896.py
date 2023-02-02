import math
n=int(input())

def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    return 1

def right_prime(n):
    b = n+1
    count=1
    while is_prime(b)==0:
        count+=1
        b+=1
    return count

def left_prime(n):
    b = n-1
    count=1
    while is_prime(b)==0:
        count+=1
        b-=1
    return count
        
for i in range(n):
    x=int(input())
    if is_prime(x)-1:
        print(right_prime(x)+left_prime(x))
    else:
        print(0)
  
    


    
        
        
    