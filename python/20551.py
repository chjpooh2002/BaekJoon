import sys
input = sys.stdin.readline

n,m=map(int,input().split())

def lower_bound(my_list,k) :
    left,right=0,len(my_list)-1
    while left <= right :
        mid = (left + right) // 2
        if my_list[mid] < k :
            left = mid + 1
        elif my_list[mid] > k  :
            right = mid - 1
        elif my_list[mid] == k :
            if right == mid :
                break
            right = mid
    if my_list[mid] == k :
        return mid
    else :
        return -1

x=sorted([int(input()) for i in range(n)])
for i in range(m):
    b=int(input())
    print(lower_bound(x,b))
