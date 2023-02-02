import sys
input = sys.stdin.readline

def check_palin(number):             
    for i in range(len(number) // 2):      
        if number[i] != number[-1 - i]:     
            return 0
    return 1

while True:
    n=int(input())
    if n==0:
        break
    if check_palin(str(n)):
        print("yes")
    else:
        print("no")