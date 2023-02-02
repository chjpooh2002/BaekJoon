import sys
input = sys.stdin.readline

def binary_search(array, target):
    start,end = 0,len(array)-1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return 0

n,m=map(int,input().split())
count=0
x=[input() for i in range(n)]
x.sort()
z=[]
for i in range(m):
    a=input()
    if binary_search(x, a):
        count+=1
        z.append(a)
z.sort()
print(count)
for i in z:
    i = i.strip()
    print(i)

    
    


