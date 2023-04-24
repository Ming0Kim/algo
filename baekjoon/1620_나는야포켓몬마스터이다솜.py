N, M = map(int, input().split())

pocketmon = [0]
for _ in range(N):
    pocketmon.append(input())

for _ in range(M):
    inputs = input()
    if inputs.isdigit():
        print(pocketmon[int(inputs)])
    else:
        print(pocketmon.find(inputs))