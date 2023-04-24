th = 0
title = 0

N = int(input())

while True:
    if '666' in str(title):
        th += 1
        if N == th:
            print(title)
            break
        else:
            title += 1
    else:
        title += 1