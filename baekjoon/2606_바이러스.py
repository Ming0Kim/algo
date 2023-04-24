from collections import deque

def bfs(N):
    cnt = 0
    visited = []
        

computer = int(input())
link = int(input())
adj = [[] for _ in range(computer+1)]

for _ in range(link):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
# print(adj)

q = deque()

