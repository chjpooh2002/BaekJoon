n = int(input())

def check_palin(number):             
    for i in range(len(number) // 2):      
        if number[i] != number[-1 - i]:     
            return 0
    return 1
 
def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    if n==1:
        return 0
    return 1
    
while True:
    if check_palin(str(n)) and is_prime(n):
        print(n)
        break
    n+=1
