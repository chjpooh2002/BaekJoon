import sys
input = sys.stdin.readline

n=int(input())

dp=[1 for i in range(n)]

x=list(map(int,input().split()))
for i in range(n):
    for j in range(i):
        if x[j]>x[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))