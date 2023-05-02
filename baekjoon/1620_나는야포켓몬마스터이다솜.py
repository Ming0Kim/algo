import sys
input = sys.stdin.readline

N, M = map(int, input().split())

enc = {}

for i in range(1, N+1):
    pocketmon = input().rstrip()
    enc[pocketmon] = str(i)
    enc[str(i)] = pocketmon

for _ in range(M):
    question = input().rstrip()
    print(enc[question])