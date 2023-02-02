import sys
import math
input = sys.stdin.readline

def eratos(a):
    n = 2*a
    count=0
    array = [True for i in range(n + 1)]
    for i in range(2, int(math.sqrt(n)) + 1): 
        if array[i] == True:
            j = 2 
            while i * j <= n:
                array[i * j] = False
                j += 1
    for i in range(2, n + 1):
        if array[i] and i>=a+1:
            count+=1
    return count

while True:
    n=int(input())
    if n==0:
        break
    print(eratos(n))
    
    