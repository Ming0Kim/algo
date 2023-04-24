from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N, M, V = map(int, input().split())
adj = [[] * (N+1) for _ in range(N+1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

for i in adj:
    i.sort()

visited = [0] * (N+1)
def dfs(d):
    print(d, end=' ')
    visited[d] = 1
    for i in adj[d]:
        if not visited[i]:
            dfs(i)
dfs(V)

print()

visited = [0] * (N+1)
def bfs(b):
    q = deque([b])
    visited[b] = 1
    while q:
        a = q.popleft()
        print(a, end=' ')
        for i in adj[a]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
bfs(V)