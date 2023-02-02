import sys
input = sys.stdin.readline
n=int(input())
x=[]
while n>0:
    x.append(n%10)
    n=n//10
x.sort(reverse = True)
for i in x:
    print(i,end="")