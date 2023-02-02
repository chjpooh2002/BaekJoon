import sys
sys.setrecursionlimit(2*10**5)
input = sys.stdin.readline

N,M,start=map(int,input().split())
visited = [False for i in range(N+1)]
visited[0]=True
count=1
graph = [[] for i in range(N+1)]
visit_count=[0 for i in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node) :
    global count
    if not visited[node] :#재귀
        visited[node] = True
        visit_count[node]=count
        count+=1
    x=graph[node].copy()
    x.sort()
    for d in x :
        if not visited[d] :
            visited[d] = True
            visit_count[d]=count
            count+=1
            dfs(d)

dfs(start)
for i in range(1,N+1):
    if visited[i]==False:
        print(0)
    else:
        print(visit_count[i])
