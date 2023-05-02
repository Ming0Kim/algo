escape = 1 # 벌집 수
num = 1    # 계산한 숫자

N = int(input())
while True:
    if N > num:
        num += 6 * escape
        escape += 1
    else:
        print(escape)
        break

