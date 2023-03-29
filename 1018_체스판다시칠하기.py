N, M = map(int, input().split())
chess = [list(input()) for _ in range(N)]

result = 64

for i in range(N-7):
    for j in range(M-7):
        # 다시 칠해야 하는 정사각형 초기화
        brush = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if a%2:
                    if b%2:
                        if chess[a][b] != 'W':
                            brush += 1
                    else:
                        if chess[a][b] != 'B':
                            brush += 1
                else:
                    if b%2:
                        if chess[a][b] != 'B':
                            brush += 1
                    else:
                        if chess[a][b] != 'W':
                            brush += 1
        # 첫 칸이 'W', 'B' 둘 중의 최소값
        min_brush = min(brush, 64-brush)
        if min_brush < result:
            result = min_brush
print(result)