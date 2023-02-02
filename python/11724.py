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
                
N,M=map(int,input().split())
count=0
visted = [False for i in range(N+1)]
visted[0]=True
graph = [[] for i in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

while visted.count(False)!=0:
    bfs(visted.index(False))
    count+=1
    
'''
for i in range(1,N+1) :
    if not visited[i] :
        bfs(i)
        count += 1
'''
print(count)