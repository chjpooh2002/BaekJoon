import sys
input = sys.stdin.readline

a,b=map(int,input().split())
count=0
while a!=b:
    if b%10==1:
        b=b//10
        count+=1
    elif b%2==0:
        b=b//2
        count+=1
    else:
        count=0
        print(-1)
        break
    if b<a:
        count=0
        print(-1)
        break

if count!=0:
    print(count+1)
        
        