from collections import deque
import sys
input = sys.stdin.readline

N,M,start=map(int,input().split())
visited = [False for i in range(N+1)]
graph = [[] for i in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node) :
    if not visited[node] :#재귀
        visited[node] = True
        print(node,end=" ")
    x=graph[node].copy()
    x.sort()
    for d in x :
        if not visited[d] :
            visited[d] = True
            print(d,end=" ")
            dfs(d)

def bfs(start):
    Q=deque()
    Q.append(start)
    visted1 = [False for i in range(N+1)]
    while Q:
        node = Q.popleft()
        print(node,end=" ")
        visted1[node] = True
        y=graph[node].copy()
        y.sort()
        for d in y:
            if not visted1[d]:
                visted1[d] = True
                Q.append(d)

dfs(start)
print()
bfs(start)
