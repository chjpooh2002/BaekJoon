import sys
input = sys.stdin.readline

n = int(input())
def fec(n):
    x=1
    for i in range(2,n+1):
        x*=i
    return x

a=fec(n)
count=0
while True:
    if a%10==0:
        count+=1
        a=a//10
    else:
        break
print(count)