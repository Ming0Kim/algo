N, M, V = map(int, input().split())
adj = [[0] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)

for i in adj:
    i.sort()

# DFS
dfs_visited = 