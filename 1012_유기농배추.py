from collections import deque

T = int(input())
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for _ in range(T):
    M, N, K = map(int, input().split())
    cnt = 0

    field = [[0]*N for j in range(M)]
    # print(field)
    for i in range(K):
        X, Y = map(int, input().split())
        field[X][Y] = 1
        # print(field)

    Q = deque()
    for x in range(M):
        for y in range(N):
            if field[x][y] == 1:
                Q.append((x, y))
                field[x][y] = 0
                while Q:
                    (A, B) = Q.pop()
                    for d in direction:
                        if 0 <= A+d[0] < M and 0<= B+d[1] < N and field[A+d[0]][B+d[1]] == 1:
                            Q.append((A+d[0], B+d[1]))
                            field[A+d[0]][B+d[1]] = 0
                cnt += 1
    print(cnt)