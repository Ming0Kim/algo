X = int(input())

DP = [1000000] * (X+1)
DP[0], DP[1] = 0, 0

for i in range(2, X+1):
    if i%3==0:
        DP[i] = min(DP[i], DP[i//3] + 1)
    if i%2==0:
        DP[i] = min(DP[i], DP[i//2]+1)
    DP[i] = min(DP[i], DP[i-1]+1)

print(DP[X])