from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    Q=deque()
    Q.append(start)
    while Q:
        node = Q.popleft()
        visted[node] = True
        for d in graph[node]:
            if not visted[d]:
                visted[d] = True
                Q.append(d)
                
N=int(input())
M=int(input())
visted = [False for i in range(N+1)]
graph = [[] for i in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)
print(visted.count(True)-1)
    
