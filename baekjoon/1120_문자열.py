A, B = input().split()
N, M = len(A), len(B)

mx = M

for i in range(M-N+1):
    cnt = 0
    for j in range(N):
        if A[j] != B[j+i]:
            cnt += 1
    if cnt <= mx:
        mx = cnt

print(mx)
